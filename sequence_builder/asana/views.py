from django.http import HttpRequest
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Asana
from .serializers import AsanaSerializer


class AsanaViewSet(viewsets.GenericViewSet):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    queryset = Asana.objects.all()

    def list(self, request: HttpRequest):
        asanas = self.get_queryset()
        serializer = AsanaSerializer(asanas, many=True)

        return Response(serializer.data)

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
        asana = self.get_object()
        serializer = AsanaSerializer(asana)

        return Response(serializer.data)

    def update(self, request, pk=None):
        asana = self.get_object()

        name = request.data.get("name", "")
        description = request.data.get("description", "")
        image = request.data.get("image", "")

        asana.name = name
        asana.description = description

        if image != "undefined":
            asana.image = image

        serializer = AsanaSerializer(asana, partial=True)

        asana.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        asana = self.get_object()
        asana.delete()

        return Response(status.HTTP_204_NO_CONTENT)
