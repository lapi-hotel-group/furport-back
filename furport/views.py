from django.db import models
from rest_framework import permissions, renderers, viewsets, mixins
from rest_framework.decorators import action
from django.contrib.auth.models import User

from furport.models import Event, GeneralTag, CharacterTag, OrganizationTag, Profile
from furport.serializers import (
    EventSerializer,
    UserSerializer,
    ProfileSerializer,
    GeneralTagSerializer,
    CharacterTagSerializer,
    OrganizationTagSerializer,
)
from furport.permissions import IsOwnerOrReadOnly, IsUserOrReadOnly, ReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.annotate(
        stars=models.Count("star"), attends=models.Count("attend")
    )
    serializer_class = EventSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    @action(detail=False, methods=["post"])
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GeneralTagViewSet(viewsets.ModelViewSet):
    queryset = GeneralTag.objects.all()
    serializer_class = GeneralTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CharacterTagViewSet(viewsets.ModelViewSet):
    queryset = CharacterTag.objects.all()
    serializer_class = CharacterTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrganizationTagViewSet(viewsets.ModelViewSet):
    queryset = OrganizationTag.objects.all()
    serializer_class = OrganizationTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
