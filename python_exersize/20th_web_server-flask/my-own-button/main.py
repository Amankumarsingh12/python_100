from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/press_button')
def press_button():
    print("Hi!")
    return "Hi!"

@app.route('/release_button')
def release_button():
    print("Bye!")
    return "Bye!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

