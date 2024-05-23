from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1>' \
            '<p> this </p>' \
            '<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmhsdjF2b3k1czdzOWNzeThvemFqOWQyZW41YWloZTJmdzZ3dDVlZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LzwcNOrbA3aYvXK6r7/giphy.gif" width=200>'


@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"hello {name}"

@app.route("/<name>")
def greet2(name):
    return f"hello {name}"

if __name__ == "__main__":
    app.run(debug=True)



