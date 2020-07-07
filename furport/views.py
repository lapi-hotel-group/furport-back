from rest_framework import permissions, renderers, viewsets, mixins
from rest_framework.decorators import action

from furport.models import Event, Tag
from furport.serializers import (
    EventSerializer,
    TagSerializer,
)
from furport.permissions import IsOwnerOrReadOnly


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
