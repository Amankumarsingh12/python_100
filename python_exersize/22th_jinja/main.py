from flask import Flask, render_template
import random
import datetime


app = Flask(__name__)

@app.route("/")
def home():
    rand_int = random.randint(1, 10)
    # current_year = datetime.datetime.now().year
    current_year = datetime.datetime.now()
    return render_template("index.html", num=rand_int, year=f"ak singh {current_year}")



if __name__ == "__main__":
    app.run(debug=True)