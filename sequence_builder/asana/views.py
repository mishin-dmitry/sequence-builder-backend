from django.http import HttpRequest
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

# from .models import Asana
from .serializers import AsanaSerializer


class AsanaViewSet(viewsets.ViewSet):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def create(self, request: HttpRequest):
        name = request.data.get("name", "")
        description = request.data.get("description", "")
        image = request.data.get("image", "")

        serializer = AsanaSerializer(
            data={"name": name, "description": description, "image": image}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
