from pprint import pprint

from elastic_process import ElasticProcess
from process_data import Processor
from config.config import URL_ELASTIC
from mapping import maping
from connection import get_es_client
from elasticsearch.exceptions import ConnectionError, NotFoundError
from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import scan
from loader import Loader



class Manager:

    def __init__(self):
        self.es = get_es_client()
        self.elastic = ElasticProcess()
        self.data = self.elastic.data


    def main(self):
        for document in self.data:
            print(document)
            id = document['id']
            field = 'sentiment'
            val = self.elastic.sentiment(document["text"])
            update_data = self.elastic.update_field_in_doc(id,field,val)
            pprint(document)
        return self.data

if __name__ == "__main__":
    m = Manager()
    m.main()

