import os
from pprint import pprint
from connection import get_es_client
from elasticsearch.exceptions import ConnectionError, NotFoundError
from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import scan
from loader import Loader
from config.config import URL_ELASTIC
from config.config import MY_INDEX
from process_data import Processor

ES_HOST = os.getenv('URL_ELASTIC',  "")


class ElasticProcess:

    def __init__(self):
        self.loader = Loader()
        self.es = get_es_client()
        self.data = self.get_all_data()
        self.index =MY_INDEX
        self.es.indices.delete(index=MY_INDEX, ignore_unavailable=True)
        self.es.indices.create(index=MY_INDEX)

    def insert_documents(self):
        #
        res = helpers.bulk(self.es, self.data)
        return res


    def get_all_data(self):
        documents = []
        for doc in scan(self.es, index=MY_INDEX):
            documents.append(doc['_source'])
        return documents


    # for document in self.data:
#     doc_id = document["_id"]
#     index_name = MY_INDEX
#     score = self.sentiment(document['_source']['text'])


    def update_field_in_doc(self,id ,field_to_update, value):
            update_body = {
                "doc": {
                    field_to_update: value
                }}
            response = self.es.update(index=MY_INDEX, id=id, body=update_body)
            print(response)


    def sentiment(self,text):
        process = Processor()
        score = process.score_text_sentiment(text)
        sentiment = process.score_sentiment_to_df(score)
        return sentiment





#
c = ElasticProcess()
# print(c.data)
c.insert_documents()
# c.get_all_data()
# c.update_field_in_doc('sentiment', "happy")