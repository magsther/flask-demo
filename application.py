from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This app is deployed in Azure. Pretty cool "
