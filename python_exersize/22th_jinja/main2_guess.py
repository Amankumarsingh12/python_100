from flask import Flask, render_template
import random
import datetime
import requests
import json


app = Flask(__name__)

@app.route("/")
def home():
    rand_int = random.randint(1, 10)
    # current_year = datetime.datetime.now().year
    current_year = datetime.datetime.now()
    return render_template("index.html", num=rand_int, year=f"ak singh {current_year}")

@app.route("/guess/<name>") 
def greet(name):
    URL_GENDER = f"https://api.genderize.io?name={name}"
    URL_AGE = f"https://api.agify.io/?name={name}"

    respond = requests.get(url=URL_GENDER)
    respond.raise_for_status()
    data = respond.json()
    gender = data["gender"]

    respond = requests.get(url=URL_AGE)
    respond.raise_for_status()
    data = respond.json()
    age = data["age"]

    return render_template("age_gender.html", my_name = f"hey {name}", my_gender = gender, my_age = age)


if __name__ == "__main__":
    app.run(debug=True)