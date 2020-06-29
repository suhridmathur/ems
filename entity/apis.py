from entity.models import Entity
from entity.tasks import index_entity
from entity.serializers import EntitySerializer
from search.service import SearchService

from rest_framework.response import Response
from rest_framework import viewsets, views


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


class MultiTagSearchAPI(views.APIView):
    """
    Returns all entities from the elasticsearch which
    have all the searched tags present into their documents.
    """

    def get(self, request, *args, **kwargs):
        """
        For multiple tags search use query parameter `tags`.
        Example: /api/entities/newspaper/?tags=toi,ht
        """
        tag = kwargs.get("tag")

        try:
            tags = self.request.query_params.get("tags").split(",")
            tags.append(tag)
        except AttributeError:
            tags = [tag]

        result = SearchService().multi_term_search("tags.keyword", tags)
        return Response(result["hits"]["hits"])
