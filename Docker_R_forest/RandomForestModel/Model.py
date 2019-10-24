# Created on 2019-10-15 13:41:09
# @author: Srihari Kodam

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,recall_score,confusion_matrix,auc,accuracy_score
import pandas as pd
import scipy.stats as st


## Load Data
iris= datasets.load_iris()
X= iris.data
Y=iris.target

## Train Test split of data

x_train,x_test,y_train,y_test= train_test_split(X,Y,test_size=0.3,random_state=42)

## Train Model
clf= RandomForestClassifier(n_estimators=3)

clf.fit(x_train,y_train)
## Test the model on test datasets
y_pred=clf.predict(x_test)
## Generate metrics on test dataset
print(accuracy_score(y_test,y_pred),accuracy_score(y_test,y_pred))
## Convert model to pickel file, serial file

import pickle
with open('/home/intel/Documents/flask_docker_practice/RandomForestModel/rf.pkl','wb') as model_pkl:
    pickle.dump(clf,model_pkl)

## Use Flask to make model available as webservices
