from django.urls import include, path
from rest_framework import routers

from furport import views


router = routers.DefaultRouter()
router.register(r"events", views.EventViewSet)
router.register(r"tags", views.TagViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
]
