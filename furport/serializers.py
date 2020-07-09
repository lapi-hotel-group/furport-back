from rest_framework import serializers
from django.contrib.auth.models import User, Permission

from furport.models import Event, GeneralTag, OrganizationTag, CharacterTag, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "url", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Profile.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class GeneralTagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = GeneralTag
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class CharacterTagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CharacterTag
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class OrganizationTagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = OrganizationTag
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class EventSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    id = serializers.ReadOnlyField()
    stars = serializers.IntegerField(required=False)
    attends = serializers.IntegerField(required=False)

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
