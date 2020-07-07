from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from furport import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", obtain_jwt_token),
]
