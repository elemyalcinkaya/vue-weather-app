from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weather")
def get_weather(city: str):
    print("API KEY:", API_KEY)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    print("URL:", url)
    response = requests.get(url)
    print("API response:", response.text)
    if response.status_code != 200:
        return {"error": "Şehir bulunamadı veya API hatası"}
    return response.json()
