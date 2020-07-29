from django.db import models
from rest_framework import permissions, renderers, viewsets, mixins, filters
from rest_framework.views import APIView
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.social_serializers import TwitterConnectSerializer

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


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter


class UserViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["username"]


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

    def get_queryset(self):
        queryset = Profile.objects.select_related("user").annotate(
            events_created=models.Count("user__created_by")
        )
        username = self.request.query_params.get("username", None)
        q_ids = self.request.query_params.get("q_ids", None)
        my_follow = self.request.query_params.get("my_follow", None)
        if username is not None:
            queryset = queryset.filter(user__username__iexact=username)
        if q_ids is not None:
            queryset = queryset.filter(user__id__in=q_ids.split(","))
        if my_follow is not None:
            queryset = queryset.filter(
                user__id__in=self.request.user.profile.following.all()
            )
        return queryset


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["start_datetime", "end_datetime", "stars", "attends"]

    @action(detail=False, methods=["post"])
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        queryset = Event.objects.annotate(
            stars=models.Count("star", distinct=True)
        ).annotate(attends=models.Count("attend", distinct=True))
        general_tag = self.request.query_params.get("general_tag", None)
        character_tag = self.request.query_params.get("character_tag", None)
        organization_tag = self.request.query_params.get("organization_tag", None)
        created_by = self.request.query_params.get("created_by", None)
        min_start_datetime = self.request.query_params.get("min_start_datetime", None)
        max_start_datetime = self.request.query_params.get("max_start_datetime", None)
        min_end_datetime = self.request.query_params.get("min_end_datetime", None)
        max_end_datetime = self.request.query_params.get("max_end_datetime", None)
        q_ids = self.request.query_params.get("q_ids", None)
        search = self.request.query_params.get("search", None)
        my_attend = self.request.query_params.get("my_attend", None)
        if general_tag is not None:
            queryset = queryset.filter(general_tag__name__iexact=general_tag)
        if character_tag is not None:
            queryset = queryset.filter(character_tag__name__iexact=character_tag)
        if organization_tag is not None:
            queryset = queryset.filter(organization_tag__name__iexact=organization_tag)
        if created_by is not None:
            queryset = queryset.filter(created_by__username__iexact=created_by)
        if min_start_datetime is not None:
            queryset = queryset.filter(start_datetime__gt=min_start_datetime)
        if max_start_datetime is not None:
            queryset = queryset.filter(start_datetime__lt=max_start_datetime)
        if min_end_datetime is not None:
            queryset = queryset.filter(end_datetime__gt=min_end_datetime)
        if max_end_datetime is not None:
            queryset = queryset.filter(end_datetime__lt=max_end_datetime)
        if q_ids is not None:
            queryset = queryset.filter(id__in=q_ids.split(","))
        if my_attend is not None:
            queryset = queryset.filter(attend__user=self.request.user)
        if search is not None:
            queryset = queryset.filter(
                models.Q(name__icontains=search)
                | models.Q(general_tag__name__icontains=search)
                | models.Q(character_tag__name__icontains=search)
                | models.Q(organization_tag__name__icontains=search)
                | models.Q(google_map_description__icontains=search)
                | models.Q(search_keywords__icontains=search)
            )
        return queryset


class GeneralTagViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = GeneralTag.objects.all()
    serializer_class = GeneralTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CharacterTagViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = CharacterTag.objects.all()
    serializer_class = CharacterTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrganizationTagViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = OrganizationTag.objects.all()
    serializer_class = OrganizationTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
