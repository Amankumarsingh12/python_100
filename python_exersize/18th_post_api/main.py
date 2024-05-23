import requests
from datetime import datetime

USERNAME = "aksingh"
TOKEN = "amanamanamanaman"
GRAPH_ID = "aman1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
    }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# #{"message":"Success. Let's visit https://pixe.la/@aksingh , it is your profile page!","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_conf = {
    "id" : GRAPH_ID,
    "name" : "Aksingh",
    "unit" : "km",
    "type" : "float",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN,

}

# response = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)
# print(response.text)
# #https://pixe.la/v1/users/aksingh/graphs/aman1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "9.74",

}

today_data = today.strftime("%Y%m%d")

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_data}"

new_pixel_data = {
    "quantity" : "17",

}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)