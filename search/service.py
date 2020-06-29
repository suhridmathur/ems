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
        return "entity"

    def __init__(self):
        self.es = Elasticsearch(
            host=settings.ELASTICSEARCH_CONFIG["HOST"],
            port=settings.ELASTICSEARCH_CONFIG["PORT"],
        )

    def index_document(self, document):
        result = self.es.index(self.index_name, body=document)
        return result

    def index_document_with_id(self, id, document):
        result = self.es.index(self.index_name, id=id, body=document)
        return result

    def multi_term_search(self, field, values):
        """
        Searches for documents which have all the `values`
        present in their `field`.
        """
        must_list = [{"term": {field: value}} for value in values]
        dsl_query = {
            "query": {
                "bool": {
                    "must": must_list
                }
            }
        }
        return self.es.search(index=self.index_name, body=dsl_query)

    def auto_complete(self, field_name, value, sort_by="created", order="desc"):
        """
        Performs boolean search.
        Searches using fuzzy search & prefix search.
        """
        dsl_query = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "fuzzy": {
                                field_name: {
                                    "value": value,
                                    "fuzziness": 7,
                                    "prefix_length": 0,
                                    "max_expansions": 50,
                                }
                            }
                        },
                        {
                            "prefix": {
                                field_name: value
                            }
                        },
                    ],
                    "minimum_should_match": 1,
                }
            }
        }
        return self.es.search(index=self.index_name, body=dsl_query)
