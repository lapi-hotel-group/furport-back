from django.urls import include, path, re_path
from rest_framework import routers, permissions
from rest_auth.registration.views import (
    SocialAccountListView,
    SocialAccountDisconnectView,
)
from allauth.socialaccount.views import ConnectionsView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from furport import views


router = routers.DefaultRouter()
router.register(r"events", views.EventViewSet, basename="event")
router.register(r"general_tags", views.GeneralTagViewSet)
router.register(r"character_tags", views.CharacterTagViewSet)
router.register(r"organization_tags", views.OrganizationTagViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"profiles", views.ProfileViewSet, basename="profile")

schema_view = get_schema_view(
    openapi.Info(
        title="FurPort API",
        default_version="v1",
        description="This documentation describes the FurPort API.",
        terms_of_service="https://www.furport.tk/terms",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("rest-auth/twitter/", views.TwitterLogin.as_view(), name="twitter_login"),
    path(
        "rest-auth/twitter/connect/",
        views.TwitterConnect.as_view(),
        name="twitter_connect",
    ),
    path(
        "accounts/social/connections/",
        SocialAccountListView.as_view(),
        name="socialaccount_connections",
    ),
    re_path(
        r"^socialaccounts/(?P<pk>\d+)/disconnect/$",
        SocialAccountDisconnectView.as_view(),
        name="social_account_disconnect",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
