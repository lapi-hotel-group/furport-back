from rest_framework import serializers
from django.contrib.auth.models import User, Permission
from drf_writable_nested.serializers import WritableNestedModelSerializer

from furport.models import Event, GeneralTag, OrganizationTag, CharacterTag, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "url")


class ProfileSerializer(serializers.ModelSerializer):
    is_moderator = serializers.ReadOnlyField()
    user = UserSerializer(read_only=True)

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


class EventSerializer(WritableNestedModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    id = serializers.ReadOnlyField()
    stars = serializers.IntegerField(required=False)
    attends = serializers.IntegerField(required=False)
    general_tag = GeneralTagSerializer(many=True)
    character_tag = CharacterTagSerializer(many=True)
    organization_tag = OrganizationTagSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
