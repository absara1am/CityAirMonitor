import os
import requests
import json
import pyttsx3

#used weatherapi.com
# Storing your API key in an environment variable and accessing it from your code is a good practice for keeping your credentials secure.
# in cmd - setx WEATHER_API_KEY "your_actual_api_key"

city = input("Enter the name of the city\n")
api_key = os.getenv("WEATHER_API_KEY")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
# print(json.dumps(wdic, indent=4))

air_quality = wdic['current']['air_quality']
pm2_5 = air_quality['pm2_5']
pm10 = air_quality['pm10']
no2 = air_quality['no2']
o3 = air_quality['o3']
us_epa_index = air_quality['us-epa-index']
co = air_quality['co']

air_quality_report = f"The air quality report shows PM2.5 at {pm2_5} μg/m³, PM10 at {pm10} μg/m³, Nitrogen Dioxide (NO2) at {no2} μg/m³, Ozone (O3) at {o3} μg/m³, Carbon Monoxide (CO) at {co} μg/m³, with a US-EPA Index of {us_epa_index}."

engine = pyttsx3.init()
engine.say(air_quality_report)
engine.runAndWait()
