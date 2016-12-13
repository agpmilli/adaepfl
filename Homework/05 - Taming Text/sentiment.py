from nltk.tokenize import TweetTokenizer
from nltk.sentiment import SentimentAnalyzer
from nltk.corpus import twitter_samples, stopwords
from nltk.sentiment.util import json2csv_preprocess
from nltk.sentiment.util import parse_tweets_set
from nltk.corpus import movie_reviews


######################### Tweeter demo #########################
def load_twitter():
    tokenizer = TweetTokenizer(preserve_case=False)
    fields = ['id', 'text']

    positive_json =  twitter_samples.abspath("positive_tweets.json")
    positive_csv = 'positive_tweets.csv'
    json2csv_preprocess(positive_json, positive_csv, fields, limit=None)

    negative_json = twitter_samples.abspath("negative_tweets.json")
    negative_csv = 'negative_tweets.csv'
    json2csv_preprocess(negative_json, negative_csv, fields, limit=None)

    neg_docs = parse_tweets_set(negative_csv, label='neg', word_tokenizer=tokenizer)
    pos_docs = parse_tweets_set(positive_csv, label='pos', word_tokenizer=tokenizer)

    return pos_docs, neg_docs

def load_movies():
    pos_docs = [(list(movie_reviews.words(pos_id)), 'pos') for pos_id in movie_reviews.fileids('pos')]
    neg_docs = [(list(movie_reviews.words(neg_id)), 'neg') for neg_id in movie_reviews.fileids('neg')]
    return pos_docs, neg_docs   


def train_classifier(classifier, pos_set, neg_set):
    return 0
