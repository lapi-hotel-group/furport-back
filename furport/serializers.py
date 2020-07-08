from rest_framework import serializers
from django.contrib.auth.models import User, Permission

from furport.models import Event, Tag, TagGroup, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "url")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class TagGroupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TagGroup
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class EventSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    id = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
