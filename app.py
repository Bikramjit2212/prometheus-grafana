from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
#metric counter
REQUEST_COUNT= Counter('http_request_total', "Total HTTP Requests")

@app.route("/")
def hello():
    REQUEST_COUNT.inc() #increase count on every req
    return "Hello from Python App"

def metrics():
    return generate_latest(),200, {'Content-Type':'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)