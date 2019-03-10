import numpy
import pandas
import graphviz 
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn import datasets
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split 



headers = ["target", "handicapped_infants", "water_project",
           "adoption_budget", "physician_fee_freeze",
           "el_salvador_aid", "religious_groups_in_schools",
           "anti_satellite_ban", "aid_to_nicaraguan",
           "mx_missile", "immigration", "synfuels_cutback", 
           "education_spending", "superfund_sue", "crime", 
           "duty_free_exports", "export_africa"]
features = ["handicapped_infants", "water_project",
           "adoption_budget", "physician_fee_freeze",
           "el_salvador_aid", "religious_groups_in_schools",
           "anti_satellite_ban", "aid_to_nicaraguan",
           "mx_missile", "immigration", "synfuels_cutback", 
           "education_spending", "superfund_sue", "crime", 
           "duty_free_exports", "export_africa"]
    

data = pandas.read_table("voting.txt", 
                             sep=',',
                             header = None, 
                             na_values = ["?"],
                             names = headers)


data.isna().sum()
data.isnull().sum(axis=1)



for item in features:
    data[item] = data[item].map({"n": 0, "y": 1})
data = data.fillna(3)
data["target"] = data["target"].map({"democrat": 0, "republican": 1})


X = data.drop(columns=["target"]).as_matrix()
y = data["target"].as_matrix().flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {}".format(accuracy))

print(confusion_matrix(y_test, y_pred),"\n")

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names = features,  
                         class_names = "target",  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph


from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())