from rest_framework import serializers

from .models import Asana


class AsanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asana
        fields = ["pk", "name", "description", "created_at", "image"]
