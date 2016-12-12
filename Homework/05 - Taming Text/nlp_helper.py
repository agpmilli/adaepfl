import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pycountry

a2_name = {}
a3_name = {}
for c in pycountry.countries:
    a2_name[c.alpha_2] = c.name
    a3_name[c.alpha_3] = c.name

names = [c.name for c in pycountry.countries]
lowers = map(lambda s: s.lower(), names)
lower_to_name = {}
for c in pycountry.countries:
    lower_to_name[c.name.lower()] = c.name

def concat_subj_txt(row):
    subj = '' if pd.isnull(row.ExtractedSubject) else row.ExtractedSubject
    text = '' if pd.isnull(row.ExtractedBodyText) else row.ExtractedBodyText
    return subj+text

def extract_country(row):
    countries = []
    for w in row.text:
        if w in a2_name.keys():
            countries.append(a2_name[w])
        if w in a3_name.keys():
            countries.append(a3_name[w])
        if w in names:
            countries.append(w)
        if w in lowers:
            countries.append(lower_to_name[w])
    return list(set(countries))

def bigram_search(row):
    old = row.countries
    countries = []
    for w in row.bigrams:
        if w in a2_name.keys():
            countries.append(a2_name[w])
        if w in a3_name.keys():
            countries.append(a3_name[w])
        if w in names:
            countries.append(w)
        if w in lowers:
            countries.append(lower_to_name[w])
    return list(set(old + countries))

def trigram_search(row):
    old = row.countries
    countries = []
    for w in row.trigrams:
        if w in a2_name.keys():
            countries.append(a2_name[w])
        if w in a3_name.keys():
            countries.append(a3_name[w])
        if w in names:
            countries.append(w)
        if w in lowers:
            countries.append(lower_to_name[w])
    return list(set(old + countries))

def classic_cloud(text):
    wordcloud = WordCloud(background_color="white").generate(text)
    plt.figure(figsize=(10,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def img_cloud(text, img):
    img = Image.open(img)
    img = img.resize((980,1080), Image.ANTIALIAS)
    hcmask = np.array(img)
    wordcloud = WordCloud(background_color="white", max_words=2000, mask=hcmask).generate(text)
    plt.figure(figsize=(10,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
