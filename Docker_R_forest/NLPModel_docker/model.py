#!/usr/bin/env python3
#@ author:srihari

from stemming.porter2 import stem
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from flask import Flask,request,make_response,send_file
import time
import zipfile

app= Flask(__name__)

def cleanse_text(text):
    if text:
        #whitespaces
        clean=' '.join(text.split())
        #stemming
        red_text= [stem(word) for word in clean.split()]
        #Done return
        return ' '.join(red_text)

    else:
        return text

@app.route("/cluster",method=['POST'])
def cluster():
    data= pd.read_csv(request.files['dataset'])
    ##
    #Doc Rating
    #...  4
    #...  5
    #...  3.5
    unstructure ='text'
    if 'col' in request.args:
        unstructure = request.args.get('col')
    no_of_clusters=2
    if 'no_of_clusters' in request.args:
        no_of_clusters=request.args.get('no_of_clusters')
    data= data.fillna("NULL")
    data['clean_sum']= data[unstructure].apply(cleanse_text)
    vectorizer=CountVectorizer(analyzer='word',stop_words='english')
    counts=vectorizer.fit_transform(data['clean_sum'])
    kmeans= KMeans(n_clusters=no_of_clusters)

    data['cluster_num']=kmeans.fit_predict(counts)
    data=data.drop(['clean_sum'],axis=1)
    return "this works"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

    