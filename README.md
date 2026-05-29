# AutoValuate - Car Price Prediction System

## Overview

AutoValuate is a Machine Learning web application that predicts the selling price of used cars based on vehicle specifications such as brand, model, age, mileage, fuel type, transmission type, engine size, and other key features.

The project combines data analysis, machine learning, and web development by training a Random Forest Regression model and deploying it through a Flask web application.

---

## Features

* Predict used car prices instantly
* Interactive web interface built with Flask
* Machine Learning model trained on real-world car sales data
* Supports multiple vehicle brands and models
* Handles categorical and numerical features using Scikit-Learn pipelines
* Responsive user interface using Bootstrap

---

## Dataset

The dataset contains information about used vehicles including:

* Brand
* Model
* Vehicle Age
* Kilometers Driven
* Seller Type
* Fuel Type
* Transmission Type
* Mileage
* Engine Capacity
* Maximum Power
* Number of Seats
* Selling Price

After preprocessing:

* Removed duplicate records
* Removed unnecessary columns
* Verified missing values
* Prepared data for machine learning training

Final dataset size:

* 15,244 records
* 11 input features

---

## Exploratory Data Analysis

The following visualizations were created:

* Brand vs Selling Price
* Vehicle Age vs Selling Price
* Fuel Type vs Selling Price
* Transmission Type vs Selling Price
* Kilometers Driven vs Selling Price
* Correlation Heatmap

These analyses helped identify relationships between vehicle characteristics and market value.

---

## Machine Learning Models

### Linear Regression

R² Score:

0.694

### Random Forest Regressor

R² Score:

0.883

The Random Forest model significantly outperformed Linear Regression and was selected for deployment.

---

## Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

### Backend

* Flask
* Flask-CORS

### Frontend

* HTML5
* CSS3
* Bootstrap 4
* JavaScript (Fetch API)

---

## Project Structure

```text
AutoValuate/
│
├── app.py
├── RandomForestCarPriceModel.pkl
├── requirements.txt
│
├── dataset/
│   ├── car_dataset.csv
│   └── Cleaned_Car_data.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd AutoValuate
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Model Workflow

1. User enters vehicle information.
2. Flask receives form data.
3. Input data is converted into a Pandas DataFrame.
4. The trained Random Forest pipeline preprocesses the features.
5. The model predicts the estimated vehicle price.
6. The result is displayed on the webpage.

---

## Future Improvements

* Add dynamic model filtering based on selected brand
* Deploy application to Render or Railway
* Implement currency conversion options
* Add feature importance visualization
* Experiment with XGBoost and LightGBM models
* Improve UI/UX design
* Add prediction history and analytics dashboard

---

## Author

Ahmed

Machine Learning & Software Engineering Student

Holberton School

---

## License

This project is for educational and portfolio purposes.
