from rest_framework import permissions, renderers, viewsets, mixins
from rest_framework.decorators import action
from django.contrib.auth.models import User

from furport.models import Event, Tag, TagGroup, Profile
from furport.serializers import (
    EventSerializer,
    TagSerializer,
    UserSerializer,
    ProfileSerializer,
    TagGroupSerializer,
)
from furport.permissions import IsOwnerOrReadOnly, IsUserOrReadOnly, ReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

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
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    @action(detail=False, methods=["post"])
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TagGroupViewSet(viewsets.ModelViewSet):
    queryset = TagGroup.objects.all()
    serializer_class = TagGroupSerializer
    permission_classes = (ReadOnly,)
