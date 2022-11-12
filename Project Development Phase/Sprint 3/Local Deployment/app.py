from flask import Flask, render_template, request, url_for, redirect
import os
import pandas as pd
import numpy as np
import flask
import pickle



app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/input', methods = ["GET","POST"])
def input_page():
     
     return render_template('input.html')
 

@app.route('/dosubmit', methods = ["GET","POST"])
def dosubmit():
    if request.method == 'POST':
  
     abtest = int(request.form['abtest'])
     vehicletype = int(request.form.get('vehicle'))
     regyear = int(request.form['reg_year'])
     gearbox = int(request.form['gearBox']) 
     powerps = float(request.form['power_ps'])
     kms = float(request.form['kilometer_driven'])
     regmonth = int(request.form.get('reg_month'))
     fuelType = int (request.form.get('fuel'))
     brand = int (request.form.get('brand'))     
     damage = int (request.form[ 'carDamage'])
     to_predict_list = [[abtest,vehicletype,regyear,gearbox,powerps,kms,regmonth,fuelType,brand,damage]]
     loaded_model = pickle.load(open("finalmodel.pkl","rb"))
     result = loaded_model.predict(to_predict_list)
     ans = round(result[0],2)
     prediction = str(ans)


    return redirect(url_for('output_page',output_res = prediction))
   


@app.route('/output' ,methods = ["GET","POST"])
def output_page():
    output_res  = request.args.get('output_res')
    return render_template('output.html', prediction = output_res)






if __name__ == '__main__':
    app.run()














