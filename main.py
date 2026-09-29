import json
import os
import requests
import redis
from dotenv import load_dotenv

load_dotenv()

# Setup Redis connection
r = redis.Redis(
    host='localhost', 
    port=6379, 
    db=0, 
    decode_responses=True, 
    protocol=2  # Force RESP2 for Redis 5.x
)

# API Configuration
request_path = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
location = "London,England,UK"
date = "2020-10-19"
api_key = os.getenv("API_KEY")

# Unique cache key based on location and date
cache_key = f"weather:{location}:{date}"

# 1. Check if data exists in Redis cache
cached_data = r.get(cache_key)

if cached_data:
    print("Fetching from Redis Cache...")
    weather_data = json.loads(cached_data)
    print(f"Temperature: {weather_data['days'][0]['temp']}")
else:
    print("Cache miss. Fetching from API...")
    url = f"{request_path}{location}/{date}?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        
        # 2. Store response in Redis (expire after 1 hour / 3600 seconds)
        r.set(cache_key, json.dumps(weather_data), ex=3600)
        
        print(f"Temperature: {weather_data['days'][0]['temp']}")
    elif response.status_code == 400:
        print("400 BAD_REQUEST – The format of the API is incorrect or an invalid parameter was supplied")
    elif response.status_code == 401:
        print("401 UNAUTHORIZED – Problem with API key or subscription")
    elif response.status_code == 404:
        print("404 NOT_FOUND – Request endpoint structure invalid")
    elif response.status_code == 429:
        print("429 TOO_MANY_REQUESTS – Exceeded assigned limits")
    elif response.status_code == 500:
        print("500 INTERNAL_SERVER_ERROR – General server error")
