from asana.views import AsanaViewSet
from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("asana", AsanaViewSet, basename="asana")

app_name = "api"

urlpatterns = [
    re_path("", include(router.urls)),
]
