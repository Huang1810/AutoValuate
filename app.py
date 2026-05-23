from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained Random Forest pipeline
model = pickle.load(open('RandomForestCarPriceModel.pkl', 'rb'))

# Load dataset for dropdowns
car = pd.read_csv('dataset/Cleaned_Car_data.csv')


@app.route('/', methods=['GET'])
def index():
    brands = sorted(car['brand'].unique())
    models = sorted(car['model'].unique())
    seller_types = car['seller_type'].unique()
    fuel_types = car['fuel_type'].unique()
    transmission_types = car['transmission_type'].unique()

    return render_template(
        'index.html',
        brands=brands,
        models=models,
        seller_types=seller_types,
        fuel_types=fuel_types,
        transmission_types=transmission_types
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():

    # Get form values
    brand = request.form.get('brand')
    model_name = request.form.get('model')
    vehicle_age = float(request.form.get('vehicle_age'))
    km_driven = float(request.form.get('km_driven'))
    seller_type = request.form.get('seller_type')
    fuel_type = request.form.get('fuel_type')
    transmission_type = request.form.get('transmission_type')
    mileage = float(request.form.get('mileage'))
    engine = float(request.form.get('engine'))
    max_power = float(request.form.get('max_power'))
    seats = float(request.form.get('seats'))

    # ✅ FIX: Proper DataFrame with correct types
    input_data = pd.DataFrame([[
        brand,
        model_name,
        vehicle_age,
        km_driven,
        seller_type,
        fuel_type,
        transmission_type,
        mileage,
        engine,
        max_power,
        seats
    ]], columns=[
        'brand', 'model', 'vehicle_age', 'km_driven',
        'seller_type', 'fuel_type', 'transmission_type',
        'mileage', 'engine', 'max_power', 'seats'
    ])

    # Prediction
    prediction = model.predict(input_data)

    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)
