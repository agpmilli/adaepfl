import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
import numpy as np


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

def one_hot_encode(df, columns):
    new = pd.DataFrame(df)
    ohe = preprocessing.OneHotEncoder()
    

def hot_encode(df, columns):
    return False

def groups_to_lists(grouped, key):
    #return grouped.aggregate(list)
    return grouped.apply(lambda x: pd.Series(dict([[col,x[col].tolist()] for col in x if col not in [key]])))

def has_same_value(col):
    c = col.apply(lambda row: len(set(row)))
    return all(row == 1 for row in c)

def has_nan(col):
    c = col.apply(lambda row: np.isnan(row).any())
    return any(row == True for row in c)

def replace_nan_in_list(list):
    acc = []
    last = np.nan
    for l in list:
        if not np.isnan(l):
            last = l
            break
    if np.isnan(last):
        return []
    else:
        for l in list:
            if np.isnan(l):
                acc.append(last)
            else:
                acc.append(l)
    return acc

def replace_nan(col):
    return col.apply(replace_nan_in_list)
