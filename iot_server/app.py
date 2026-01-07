from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensor_data = {
    "pir": 0,
    "ldr": 0,
    "lamp": "OFF"
}

control_data = {
    "mode": "AUTO",
    "lamp": "OFF"
}

@app.route("/api/sensor", methods=["POST"])
def sensor():
    global sensor_data
    sensor_data = request.json
    return jsonify({"status": "ok"})

@app.route("/api/sensor", methods=["GET"])
def get_sensor():
    return jsonify(sensor_data)

@app.route("/api/control", methods=["GET", "POST"])
def control():
    global control_data
    if request.method == "POST":
        control_data.update(request.json)
        return jsonify({"status": "updated"})
    return jsonify(control_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
