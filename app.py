from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

model = pickle.load(open('RandomForestCarPriceModel.pkl', 'rb'))
car = pd.read_csv('dataset/Cleaned_Car_data.csv')

INR_TO_USD = 83


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        brands=sorted(car['brand'].unique()),
        models=sorted(car['model'].unique()),
        seller_types=car['seller_type'].unique(),
        fuel_types=car['fuel_type'].unique(),
        transmission_types=car['transmission_type'].unique()
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():

    input_data = pd.DataFrame([[
        request.form.get('brand'),
        request.form.get('model'),
        float(request.form.get('vehicle_age')),
        float(request.form.get('km_driven')),
        request.form.get('seller_type'),
        request.form.get('fuel_type'),
        request.form.get('transmission_type'),
        float(request.form.get('mileage')),
        float(request.form.get('engine')),
        float(request.form.get('max_power')),
        float(request.form.get('seats'))
    ]], columns=[
        'brand', 'model', 'vehicle_age', 'km_driven',
        'seller_type', 'fuel_type', 'transmission_type',
        'mileage', 'engine', 'max_power', 'seats'
    ])

    prediction_inr = model.predict(input_data)[0]
    prediction_usd = prediction_inr / INR_TO_USD

    return str(np.round(prediction_usd, 2))


if __name__ == '__main__':
    app.run(debug=True)
