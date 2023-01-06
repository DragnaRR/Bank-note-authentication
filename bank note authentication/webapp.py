from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome All"

@app.route('/predict')
def predict_note_authentication():
    
    """Bank Note Authentication
    Application authenticates whether the note is real or not based on parameters
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query 
        type: number
        required: true
    responses:
        200:
            description: Its the output value
    
    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=model.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is" + str(prediction) 

if __name__=='__main__':
    app.run()
 