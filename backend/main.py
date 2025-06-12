import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from model import recommend_crops
from weather import get_weather

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
    weather = get_weather(lat, lon)
    crops = recommend_crops(weather["temperature"], weather["humidity"], weather["rain"])
    return {"recommendations": crops, "weather": weather}


