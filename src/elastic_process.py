import os
from pprint import pprint
from connection import get_es_client
from elasticsearch.exceptions import ConnectionError, NotFoundError
from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import scan
from loader import Loader
from config.config import URL_ELASTIC
import time

ES_HOST = os.getenv('URL_ELASTIC',  "")


class ElasticProcess:

    def __init__(self):
        self.es = get_es_client()
        self.data = Loader().data
        self.es.indices.delete(index='myindex', ignore_unavailable=True)
        self.index = self.es.indices.create(index='myindex')


    def insert_documents(self):

        res = helpers.bulk(self.es, self.data)
        return res


    def get_all_data(self):
        documents = []
        for doc in scan(self.es, index="myindex"):
            documents.append(doc['_source'])
        return documents













# c = ElasticProcess()
# print(c.data)
# c.insert_documents()
# pprint(c.get_all_data())