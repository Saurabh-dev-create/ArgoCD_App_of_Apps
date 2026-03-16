from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter("flask_requests_total", "Total HTTP Requests")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Flask app deployed using ArgoCD GitOps!"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)