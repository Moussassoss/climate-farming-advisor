# main.py
from fastapi import FastAPI, Query
from weather import get_weather
from recommender import recommend_crops

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Climate-Resilient Farming Advisor API"}

@app.get("/weather")
def fetch_weather(lat: float = Query(...), lon: float = Query(...)):
    return get_weather(lat, lon)

@app.get("/recommend")
def get_recommendation(lat: float = Query(...), lon: float = Query(...)):
    weather_data = get_weather(lat, lon)
    crops = recommend_crops(weather_data)
    return {"recommendations": crops, "weather": weather_data}
