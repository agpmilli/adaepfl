import pandas as pd
from sklearn import preprocessing

"""
Label encode each column in the dataframe given as parameter
@param - df : the dataframe
@param - columns: a list of columns to encode

@return - a new dataframe with the given columns label encoded
"""
def label_encode(df, columns):
    new = df.copy()
    le = preprocessing.LabelEncoder()
    for col in columns:
        le.fit(new[col].unique())
        new[col] = le.transform(new[col])
    return new

"""
Hot encode each columns in the dataframe given as parameter
@param - df : the dataframe
@param - columns: a list of columns to encode

@return - a new dataframe with the given columns hot encoded
"""
def one_hot_encode(df, columns):
    new = df.copy()
    for col in columns:
        one_hot = pd.get_dummies(new[col])
        new = new.drop(col, axis=1)
        new = new.join(one_hot)
    return new