from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/temperature")
def temperature():
    data = request.get_json()
    value = data["value"]
    return jsonify({"accepted": True, "value": value}), 200

if __name__ == "__main__":
    app.run(debug=True)
