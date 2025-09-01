from pprint import pprint
import pandas as pd
from config.config import PATH_TO_DATA
from config.config import PATH_TO_WEAPONS_LIST


class Loader:

    def __init__(self):
        self.data = self.load_csv()
        self.weapon_list = self.load_weapons_list()

    def load_csv(self):
        data= pd.read_csv(PATH_TO_DATA)
        return data

    def load_weapons_list(self):
        weapons_list = []
        with open(PATH_TO_WEAPONS_LIST, 'r') as weapons:
            weapon= weapons.readlines()
        for wep in weapon:
            weapons_list.append(wep.lower().strip())

        return weapons_list


# l = Loader()
# pprint(l.weapon_list)