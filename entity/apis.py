from entity.models import Entity
from entity.tasks import index_entity
from entity.serializers import EntitySerializer

from rest_framework.response import Response
from rest_framework import viewsets


class EntityViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Entity instances
    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            index_entity.delay(response.data)
        return response
