```python
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', '')
OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', '')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    if not OPENWEATHER_API_KEY:
        return jsonify({'error': 'API key not configured'}), 500
    
    try:
        params = {
            'q': city,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(OPENWEATHER_BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed']
            }
            return jsonify(weather_data), 200
        elif response.status_code == 404:
            return jsonify({'error': 'City not found'}), 404
        else:
            return jsonify({'error': 'Failed to fetch weather data'}), response.status_code
            
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to connect to weather service'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```