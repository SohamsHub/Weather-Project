import os
import requests
from dotenv import load_dotenv

load_dotenv()

PLACE_URL = os.getenv("PLACE_URL")
CURRENT_WEATHER_URL = os.getenv("CURRENT_WEATHER_URL") 
DAILY_WEATHER_URL = os.getenv("DAILY_WEATHER_URL")
HOURLY_WEATHER_URL = os.getenv("HOURLY_WEATHER_URL")



def find_place(place, headers=None):
    url = PLACE_URL

    querystring = {"text": place, "language": "en"}

    response = requests.get(url, headers=headers, params=querystring)

    return response


def get_current(latitude, longitude, headers=None):
    url = CURRENT_WEATHER_URL

    querystring = {
        "lat": latitude,
        "lon": longitude,
        "timezone": "auto",
        "language": "en",
        "units": "auto",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response


def get_daily(latitude, longitude, headers=None):
    url = DAILY_WEATHER_URL
    querystring = {
        "lat": latitude,
        "lon": longitude,
        "language": "en",
        "units": "auto",
    }
    response = requests.get(url, headers=headers, params=querystring)

    return response


def get_hourly(latitude, longitude, headers=None):
    url = HOURLY_WEATHER_URL

    querystring = {
        "lat": latitude,
        "lon": longitude,
        "timezone": "auto",
        "language": "en",
        "units": "auto",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response