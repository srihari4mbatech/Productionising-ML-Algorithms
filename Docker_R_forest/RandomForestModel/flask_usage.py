# ---coding: utf-8 ---- 
# Created on 2019-10-15 15:26:50
# @author: srihari Kodam

from flask import Flask,request,jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from flasgger import Swagger
app = Flask(__name__)
swagger=Swagger(app)
# Load pickle file to model object
with open("RandomForestModel/rf.pkl",'rb') as pickle_file:
    #pickle_str=str(pickle_file)
    model= pickle.load(pickle_file,encoding='utf-8')

# Start app route and pass inputs to model as numpy array list of list.

iris=load_iris()
targets= iris.target_names

@app.route('/predict')
def prediction_fun():
    """ Example endpoint returning a prediction of iris
    This is using docstrings for specifications.
    ----
    parameters:
        - name: s_length
          in: query
          schema:
            type: number
          required: true
        - name: s_width
          in: query
          schema:
            type: number
          required: true
        - name: p_length
          in: query
          schema:
            type: number
          required: true
        - name: p_width
          in: query
          schema:
            type: number
          required: true
    responses:
        200:
            description: There is an error in prediction from model
            schema:
                id: awesome
                properties:
                    res_val:
                        type: string
                
    """       
    s_length=request.args.get("s_length")
    s_width=request.args.get("s_width")
    p_length=request.args.get("p_length")
    p_width=request.args.get("p_width")

    prediction_val=model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    print(prediction_val)   
    prediction=targets[prediction_val][0]
    return jsonify(res_val= "The iris flower pattern is "+str(prediction))


@app.route('/predict_file',methods=['POST'])
def predict_file():
    """ Example endpoint returning a prediction of iris
    This is using docstrings for specifications.
    ----
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    responses:
        200: 
            description: Iris Flower type to be predicted
            schema:
                id: awesome
                properties:
                    res_val:
                        type: string
    """
    file_path=request.files.get('input_file')
    input_data=pd.read_csv(file_path,header=None)
    prediction_val=model.predict(input_data)
    prediction=targets[prediction_val]
    return jsonify(res_val="The iris flower types predicted are "+",".join(prediction))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)