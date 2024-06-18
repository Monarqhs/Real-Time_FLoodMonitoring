from flask import Flask, render_template, jsonify
import requests
import joblib
import pandas as pd

app = Flask(__name__)

API_KEY = '4482214ed2442cdd2b6a75cd34fb0e6b'
CITY_ID = '1642911'
URL = f'http://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric'

# Load the trained model
model = joblib.load('models/weather_model.pkl')

# Load historical weather data
historical_data = pd.read_csv('data/historical_weather_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    response = requests.get(URL)
    data = response.json()

    weather_data = {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'wind_direction': data['wind']['deg'],
        'description': data['weather'][0]['description']
    }
    
    # Prepare data for prediction
    df = pd.DataFrame([weather_data])
    prediction = model.predict(df[['temperature', 'humidity', 'wind_speed', 'wind_direction']])[0]
    weather_data['predicted_rainfall'] = prediction
    
    return jsonify(weather_data)

@app.route('/heatmap-data')
def get_heatmap_data():
    # You can modify this function to prepare heatmap data based on historical_data or model predictions
    heatmap_data = []  # Placeholder, replace with your heatmap data
    return jsonify(heatmap_data)

if __name__ == '__main__':
    app.run(debug=True)
