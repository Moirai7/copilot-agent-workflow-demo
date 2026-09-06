from flask import Flask, jsonify, request

app = Flask(__name__)

MIN_TEMPERATURE = -100
MAX_TEMPERATURE = 200

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/temperature")
def temperature():
    data = request.get_json(silent=True) or {}

    if "value" not in data:
        return jsonify({"accepted": False, "error": "value is required"}), 400

    value = data["value"]

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return jsonify({"accepted": False, "error": "value must be numeric"}), 400

    if not MIN_TEMPERATURE <= value <= MAX_TEMPERATURE:
        return jsonify({
            "accepted": False,
            "error": f"value must be between {MIN_TEMPERATURE} and {MAX_TEMPERATURE}",
        }), 400

    return jsonify({"accepted": True, "value": value}), 200

if __name__ == "__main__":
    app.run(debug=True)
