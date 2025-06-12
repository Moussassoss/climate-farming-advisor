import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from model import recommend_crops

app = FastAPI()
load_dotenv()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Later, replace with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommend")
def recommend(lat: float, lon: float):
    # Fetch weather data using OpenWeatherMap API
    api_key =  os.getenv("OPENWEATHER_API_KEY")
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(weather_url)
    data = response.json()

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    rain = data.get('rain', {}).get('1h', 0) 

    # Get crop recommendations
    crops = recommend_crops(temperature, humidity, rain)

    return {
        "recommendations": crops,
        "weather": {
            "temperature": temperature,
            "humidity": humidity,
            "description": description,
            "rain": rain
        }
    }
