import requests
import json

respond = requests.get(url="https://api.agify.io/?name=aman")
respond.raise_for_status()
data = respond.json()
age = data["age"]
print(age)
