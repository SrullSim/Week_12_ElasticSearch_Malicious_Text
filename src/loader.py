import json
from pprint import pprint
import pandas as pd
from config.config import PATH_TO_DATA
from config.config import PATH_TO_WEAPONS_LIST
from config.config import MY_INDEX

import csv


class Loader:

    def __init__(self):
        self.csv_data = self.load_csv()
        self.data = self.to_elasticsearch_docs(MY_INDEX)
        self.weapon_list = self.load_weapons_list()


    def load_csv(self):
        data = []
        with open(PATH_TO_DATA,'r', newline='', encoding='utf-8') as csvfile:
            reader = list(csv.DictReader(csvfile))
        for row in reader:
            data.append(row)
        return data

    def load_weapons_list(self):
        weapons_list = []
        with open(PATH_TO_WEAPONS_LIST, 'r') as weapons:
            weapon= weapons.readlines()
        for wep in weapon:
            weapons_list.append(wep.lower().strip())
        return weapons_list


    def to_elasticsearch_docs(self, index_name):
        col = []
        for row in self.csv_data:
            doc = {
                "_index": index_name,
                "_source": row
            }
            col.append(doc)
        return col



# l = Loader()
# p=l.data
# pprint(p)
