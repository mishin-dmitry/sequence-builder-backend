from rest_framework import viewsets

from .models import Asana
from .serializers import AsanaSerializer


class AsanaViewSet(viewsets.ModelViewSet):
    serializer_class = AsanaSerializer
    queryset = Asana.objects.all()

    print(queryset)
