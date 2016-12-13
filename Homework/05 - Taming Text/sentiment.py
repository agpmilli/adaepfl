from nltk.tokenize import TweetTokenizer
from nltk.sentiment import SentimentAnalyzer
from nltk.corpus import twitter_samples, stopwords
from nltk.sentiment.util import json2csv_preprocess
from nltk.sentiment.util import parse_tweets_set
from nltk.corpus import movie_reviews
from sklearn.model_selection import train_test_split
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC
from nltk.sentiment.util import extract_unigram_feats
from nltk.sentiment.util import extract_bigram_feats
from nltk.classify import NaiveBayesClassifier
from sklearn.model_selection import train_test_split



######################### Loaders #########################
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


##################### split ##########################

def split_set(pos, neg):
    train_pos, test_pos = train_test_split(pos, test_size=0.2)
    train_neg, test_neg = train_test_split(neg, test_size=0.2)
    return train_pos+train_neg, test_pos+test_neg

def run_sa_twitt(train, test):
    a = SentimentAnalyzer()
    tr = NaiveBayesClassifier.train
    all_words = [word for word in a.all_words(train)]
    # Add simple unigram word features
    unigram_feats = a.unigram_word_feats(all_words, top_n=1000)
    a.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

    # Add bigram collocation features
    bigram_collocs_feats = a.bigram_collocation_feats([tweet[0] for tweet in train_twitt],top_n=100, min_freq=12)
    a.add_feat_extractor(extract_bigram_feats, bigrams=bigram_collocs_feats)

    tr_set = a.apply_features(train)
    test_set = a.apply_features(test)

    #Training
    clf = a.train(tr, tr_set)
    res = a.evaluate(test_set)

    print(res)

def run_sa_mov(train, test):
    a = SentimentAnalyzer()
    tr = NaiveBayesClassifier.train
    all_words = mov_analyzer.all_words(train)
    # Add simple unigram word features
    unigram_feats = a.unigram_word_feats(all_words, min_freq=4)
    a.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
    # Apply features to obtain a feature-value representation of our datasets
    tr_set = a.apply_features(train)
    test_set = a.apply_features(test)

    #Training
    clf = a.train(tr, tr_set)
    res = a.evaluate(test_set)

    print(res)
