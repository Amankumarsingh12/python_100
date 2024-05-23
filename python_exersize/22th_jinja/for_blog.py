from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("blog_index.html", num=random.randint(1, 10))


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/f46cf1d10894eebbcd3c"
    respond = requests.get(url=blog_url)
    respond.raise_for_status()
    data = respond.json()
    #print(data)
    return render_template("blog.html", posts=data)



if __name__ == "__main__":
    app.run(debug=True)