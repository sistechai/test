from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World, This is auto deploy test2'



