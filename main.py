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
elif response.status_code== 400:
    print("400 BAD_REQUEST – The format of the API is incorrect or an invalid parameter or combination of parameters was supplied")
elif response.status_code== 401:
    print("401 UNAUTHORIZED – There is a problem with the API key, account or subscription. May also be returned if a feature is requested for which the account does not have access to.")
elif response.status_code== 401:
    print("401 UNAUTHORIZED – There is a problem with the API key, account or subscription. May also be returned if a feature is requested for which the account does not have access to.")
elif response.status_code== 404:
    print("404 NOT_FOUND – The request cannot be matched to any valid API request endpoint structure.")
elif response.status_code== 429:
    print("429 TOO_MANY_REQUESTS – The account has exceeded their assigned limits.")
elif response.status_code== 500:
    print("500 INTERNAL_SERVER_ERROR – A general error has occurred processing the request.")


