import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
response.raise_for_status()

data = response.json()
print(data)

longi = data["iss_position"]["longitude"]
lati = data["iss_position"]["latitude"]
iss_pos = (longi, lati)
print(iss_pos)