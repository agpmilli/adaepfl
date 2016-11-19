import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score


def drop_columns(df, columns):
    new = pd.DataFrame(df)
    for col in columns:
        new = new.drop(col, axis=1)
    return new

def fill_na_columns(df, columns, filling):
    new = pd.DataFrame(df)
    for i in range(len(columns)):
        new[columns[i]].fillna(filling[i], inplace=True)
    return new

def label_encode(df, columns):
    new = pd.DataFrame(df)
    le = preprocessing.LabelEncoder()
    for col in columns:
        le.fit(new[col].unique())
        new[col] = le.transform(new[col])
    return new

def hot_encode(df, columns):
    return False
