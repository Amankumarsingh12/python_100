from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_with_click.html")

@app.route("/button_click")
def button_click():
    print("Clicked")
    return "Button Clicked!"

@app.route("/button")
def button_click2():
    print("meee")
    return "ak sing"




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
