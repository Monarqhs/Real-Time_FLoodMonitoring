import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
data = pd.read_csv('data/historical_weather_data.csv')

# Features and target
X = data[['temperature', 'humidity', 'wind_speed', 'wind_direction']]
y = data['rainfall']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/weather_model.pkl')
print("Model trained and saved.")
