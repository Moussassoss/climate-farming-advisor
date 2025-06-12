# weather.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    rain = data.get('rain', {}).get('1h', 0)
    return {
        "temperature": temperature,
        "humidity": humidity,
        "rain": rain,
        "description": description
    }
