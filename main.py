import requests
#timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY
requestPath="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
location="London,England,UK"
APIkey=""#Put your API key here
response=requests.get(f"{requestPath}{location}/2020-10-19?key={APIkey}")


if response.status_code == 200:
    weatherData = response.json() 
print(weatherData)
