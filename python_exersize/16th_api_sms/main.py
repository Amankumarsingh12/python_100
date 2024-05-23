# api_key = "73704b30866e7e0f2ebc0c1f279589b1"

# web = "https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=73704b30866e7e0f2ebc0c1f279589b1"

import requests

api_key = "73704b30866e7e0f2ebc0c1f279589b1"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_param = {
    "q":"London,UK",
    "appid":api_key

    }

response = requests.get(OWN_Endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()
print(weather_data["weather"][0]['id'])

will_rain = False

if(int(weather_data["weather"][0]['id']) < 700):
    will_rain = True


if will_rain:
    print("bring umbreala")

    s = "DGTMLQ8GWV8C2UR7TYALJPZ9"
