from entity.models import Entity
from entity.serializers import EntitySerializer

from rest_framework.response import Response
from rest_framework import viewsets


class EntityViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Entity instances
    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer