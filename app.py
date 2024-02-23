from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
import pyrebase

app = Flask(__name__)

config = {
  "apiKey": "AIzaSyDZ4GU0X0KznmK3gCx8mVQqwZFjHKi46jE",
  "authDomain": "first-flask-app-7b882.firebaseapp.com",
  "projectId": "first-flask-app-7b882",
  "storageBucket": "first-flask-app-7b882.appspot.com",
  "messagingSenderId": "297760772258",
 "appId": "1:297760772258:web:8b4e08199b6571226f07fb",
  "measurementId": "G-NC80NQW7C2",
  "databaseURL": "https://first-flask-app-7b882-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

model = pickle.load(open('model.pkl', 'rb'))
heart_model = pickle.load(open('model1.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes-form.html")

@app.route('/heartdisease')
def heart_disease():
    return render_template("heart.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    feature_names = ['pregnancies', 'glucose', 'blood-pressure', 'skin-thickness', 'insulin','bmi','diabetes-pedigree','age']
    features = {name: request.form.get(name) for name in feature_names}
    final = [np.array([float(value) if value is not None else 0.0 for value in features.values()])]

    prediction = model.predict(final)
    print(prediction)

    if prediction[0] == 0:
        result = "The person is not diabetic"
    else:
        result = "The person is diabetic"

    
    data = {
        'features': features,
        'prediction': result
    }
    db.child('diabetes_predictions').push(data)

    return render_template('diabetes-form.html', pred=result)

@app.route('/calculate', methods=["POST", "GET"])
def calculate():
    feature_names = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
    features = {name: request.form.get(name) for name in feature_names}
    final = [np.array([float(features[name]) for name in feature_names])]

    prediction = heart_model.predict(final)
    print(prediction)

    if prediction[0] == 0:
        result = "You have no heart disease"
    else:
        result = "You have heart disease"

    data = {
        'features': features,
        'prediction': result
    }
    db.child('heart_disease_predictions').push(data)

    return render_template("heart.html", predict=result)

if __name__ == '__main__':
    app.run(debug=True)
