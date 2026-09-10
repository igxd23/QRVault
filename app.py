from flask import Flask, render_template, request, jsonify
import csv, os
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "scans.csv"

# Create CSV if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "qr_data"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save-scan", methods=["POST"])
def save_scan():
    data = request.json.get("qr_data")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), data])

    return jsonify({"status": "saved", "data": data})

if __name__ == "__main__":
    app.run(debug=True)
