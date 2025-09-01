from nltk.sentiment import SentimentIntensityAnalyzer
from loader import Loader
import pandas as pd


class Processor:


    def __init__(self):
        self.loader = Loader()
        self.data = self.loader.load_csv()
        self.weapons_list = self.loader.weapon_list



    def find_weapons(self, weapons_list, text):
        weapons_detected = []
        text_list = text.split(" ")
        for weapon in text_list:
            if weapon in weapons_list:
                weapons_detected.append(weapon)
        return weapons_detected


    def score_text_sentiment(self, text):
        """ return the score of the text """
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        return score["compound"]


    def score_sentiment_to_df(self, score):
        """ score the sentiment according the score given"""
        if 1 < score > 0.5 :
            return "positive"
        elif -0.49 < score > 0.49:
            return "natural"
        elif -1 < score < -0.5:
            return "negative"
        return None

