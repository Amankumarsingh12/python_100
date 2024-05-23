import requests
import json

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=17&type=boolean")
response.raise_for_status()
data = response.json()

print(type(data))
#### now save it on file ###
with open("database", "w") as file:
    json.dump(data, file, indent=4)


with open("database", "r") as file:
    file_data = json.load(file)

# this for question
#print(file_data["results"][0]["question"])


for que in file_data["results"] :
    #this will print question
    print(que["question"])

    my_input = input("enter true/false t/f :: ").lower()
    if my_input == que["correct_answer"].lower():
        print("wright")
    else:
        print("wrong")
    print("asn --> ", que["correct_answer"], "\n\n\n")

