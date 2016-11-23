"""
TODO REMOVE UNUSED IMPORT
"""
import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
import numpy as np

"""
encode the given columns using the preprocessing LabelEncoder object
We fit the encoder on the possible values and then transform our  each column.
"""
def label_encode(df, columns):
    new = df.copy()
    le = preprocessing.LabelEncoder()
    for col in columns:
        le.fit(new[col].unique())
        new[col] = le.transform(new[col])
    return new

"""
Encode the columns using the one-hot encode.
returns a new dataframe with the new created columns.
"""
def one_hot_encode(df, columns):
    new = df.copy()
    ohe = preprocessing.OneHotEncoder()
    for col in columns:
        one_hot = pd.get_dummies(new[col])
        new = new.drop(col, axis=1)
        new = new.join(one_hot)
    return new


"""
aggregate a groupby dataframe object as an array per column.
"""
def groups_to_lists(grouped, key):
    return grouped.apply(lambda x: pd.Series(dict([[col,x[col].tolist()] for col in x if col not in [key]])))
