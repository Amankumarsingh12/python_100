import requests
from datetime import datetime

parameters = {

    "lat": 28.565602,
    "lng": 77.321239,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(time_now.hour)


print(sunrise)
print(sunset)


