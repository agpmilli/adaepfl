from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.cross_validation import cross_val_score
import seaborn as sns
import matplotlib.pyplot as plt
 
def plot_importances(clf, data_in, labels_in):
    X_train, X_test, y_train, y_test = train_test_split(data_in, labels_in, test_size=0.20, random_state=0)
    importances = clf.fit(X_train, y_train).feature_importances_
    l = list(zip(importances, data_in.columns))
    l = [tup for tup in l if tup[0] >= 0.005]
    l.sort(key=lambda tup: tup[0], reverse=True)

    indices = range(len(l))
    values_out = list(map(lambda tup:tup[0], l))
    labels_out = list(map(lambda tup:tup[1], l))

    graph = sns.barplot(labels_out, values_out, palette='GnBu_d')
    graph.set_xticklabels(labels=labels_out, rotation=80)
    plt.show()
    
    return(X_train, X_test, y_train, y_test, values_out, labels_out)