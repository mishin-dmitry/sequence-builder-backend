from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Asana
from .serializers import AsanaSerializer


class AsanaViewSet(viewsets.ViewSet):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    queryset = Asana.objects.all()

    def list(self, request: HttpRequest):
        "Return all asanas list"

        serializer = AsanaSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpRequest):
        "Create asana instance"

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
        asana = get_object_or_404(self.queryset, pk=pk)
        serializer = AsanaSerializer(asana)

        return Response(serializer.data)

    def update(self, request, pk=None):
        asana = get_object_or_404(self.queryset, pk=pk)

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

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        asana = get_object_or_404(self.queryset, pk=pk)
        asana.delete()

        return Response(status.HTTP_204_NO_CONTENT)
