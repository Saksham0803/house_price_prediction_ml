import pickle
import numpy as np
from flask import Flask, render_template, request  #(render_template for using html)
from sklearn import *

app=Flask(__name__)
model = pickle.load(open('model3.pkl','rb'))


#url/
@app.route('/')
def index():
    return render_template('app.html')

@app.route('/predict' , methods=['GET','POST'])     #TO POST THE PREDICTION
def predict():
    values = [int(x) for x in request.form.values()]
    values1 = [np.array(values)]
    prediction = model.predict(values1)
    output = round(prediction[0],2)
    return render_template('app.html',prediction_text=f'Price for the house is {output}/-')

if __name__=='__main__':
    app.run(debug=True)