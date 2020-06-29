from ems.celery import app

from entity.models import Entity
from entity.serializers import EntitySerializer
from search.service import SearchService

@app.task
def index_entity(entity_dict):
    return SearchService().index_document_with_id(
        entity_dict.get('id'),
        entity_dict
    )