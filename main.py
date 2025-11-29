from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "online"}

@app.route("/api/soma", methods=["POST"])
def soma():
    data = request.json
    return {"resultado": data["a"] + data["b"]}
