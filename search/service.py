from django.conf import settings

from elasticsearch import Elasticsearch

from utils.base import Singleton

class SearchService(metaclass=Singleton):
    """
    SearchService: Singleton class to be used for making
    elasticsearch requests.
    """
    @property
    def index_name(self):
        return 'entity'

    def __init__(self):
        self.es = Elasticsearch(
            host = settings.ELASTICSEARCH_CONFIG['HOST'],
            port = settings.ELASTICSEARCH_CONFIG['PORT']
        )
    
    def index_document(self, document):
        result = self.es.index(self.index_name, body=document)
        return result
        
