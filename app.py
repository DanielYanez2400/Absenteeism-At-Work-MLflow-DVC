from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from src.Classifier.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            transportation_expense = float(request.form['transportation_expense'])
            distance_from_residence_to_work = float(request.form['distance_from_residence_to_work'])
            service_time = float(request.form['service_time'])
            age = float(request.form['age'])
            work_load_average_day = float(request.form['work_load_average_day'])
            hit_target = float(request.form['hit_target'])
            disciplinary_failure = float(request.form['disciplinary_failure'])
            education = float(request.form['education'])
            son = float(request.form['son'])
            social_drinker = float(request.form['social_drinker'])
            social_smoker = float(request.form['social_smoker'])
            pet = float(request.form['pet'])
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            body_mass_index = float(request.form['body_mass_index'])
       
            data = [transportation_expense, distance_from_residence_to_work, service_time, age, work_load_average_day, 
                    hit_target, disciplinary_failure, education, son, social_drinker, 
                    social_smoker, pet, weight, height, body_mass_index]
            data = np.array(data).reshape(1, 15)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)