from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/button_click', methods=['POST'])
def button_click():
    print("Hi!")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)