import requests
import os
from dotenv import load_dotenv
load_dotenv()
#timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY
requestPath="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
location="London,England,UK"
APIkey=os.getenv("API_KEY")
response=requests.get(f"{requestPath}{location}/2020-10-19?key={APIkey}")

weatherData=None
if response.status_code == 200:
    weatherData = response.json() 
print(weatherData["days"][0])
