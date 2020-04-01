from flask import Flask

app = Flask(__name__)

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/')
def home():
    return "Hello world to the flask app"


if __name__ == '__main__':
    app.run(debug = True)
