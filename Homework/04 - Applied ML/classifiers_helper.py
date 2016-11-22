from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.cross_validation import cross_val_score
import seaborn as sns
import matplotlib.pyplot as plt

"""
Plot the features' importance for a given classifier.

@param - clf: the classifier
@param - data_in: the input data 
@param - labels_in: the output data
@param - threshold_importance: the threshold required int the classification to plot it
"""
def plot_importances(clf, data_in, labels_in, treshold_importance):
    values_out, labels_out = importances(clf, data_in, labels_in, treshold_importance)
    graph = sns.barplot(labels_out, values_out, palette='GnBu_d')
    graph.set_xticklabels(labels=labels_out, rotation=80)
    plt.show()

"""
Fit the data for the given classifier and return the features' importance with its labels

@param - clf: the classifier
@param - data_in: the input data 
@param - labels_in: the output data
@param - threshold_importance: the threshold required int the classification to plot it

@return - the tuple (values_out, labels_out)
"""   
def importances(clf, data_in, labels_in, treshold_importance):
    #X_train, X_test, y_train, y_test = train_test_split(data_in, labels_in, test_size=0.20, random_state=0)
    importances = clf.fit(data_in, labels_in).feature_importances_
    l = [tup for tup in list(zip(importances, data_in.columns)) if tup[0] >= treshold_importance]
    l.sort(key=lambda tup: tup[0], reverse=True)

    indices = range(len(l))
    values_out = list(map(lambda tup:tup[0], l))
    labels_out = list(map(lambda tup:tup[1], l))
    
    return (values_out, labels_out)