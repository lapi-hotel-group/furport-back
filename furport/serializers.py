from rest_framework import serializers
from django.contrib.auth.models import User

from furport.models import Event, Tag


class EventSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
