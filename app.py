from concurrent.futures import thread
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])

def lastpage():
    return "Welcome to ARN"


@app.route('/', methods=["POST"])

def post():
    return "Welcome to 2nd Page"


if __name__ == "__main__":
    print(app.run(threaded=True))
    
else:
    pass
