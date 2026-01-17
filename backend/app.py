from flask import Flask, render_template, request, jsonify
import os
import random
import time

# Set template folder and static folder correctly
template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")

app = Flask(__name__, template_folder=template_path, static_folder=static_path)

@app.route('/')
def home():
    return render_template("dashboard.html")

@app.route('/scan', methods=['POST'])
def scan_url():
    data = request.json
    url = data.get("url", "")

    issues = [
        {"issue": "SQL Injection Risk", "severity": "high", "solution": "Use parameterized queries", "improvement": "Prevents database attacks"},
        {"issue": "XSS Vulnerability", "severity": "medium", "solution": "Escape user input", "improvement": "Prevents script injections"},
        {"issue": "Missing HTTPS", "severity": "high", "solution": "Enable SSL/TLS", "improvement": "Encrypts communication"},
        {"issue": "Slow Page Load", "severity": "low", "solution": "Optimize images and scripts", "improvement": "Faster loading time"},
        {"issue": "Deprecated HTML tags", "severity": "low", "solution": "Update HTML to modern standards", "improvement": "Improved browser compatibility"}
    ]

    report_data = random.sample(issues, random.randint(1, len(issues)))
    time.sleep(random.randint(2, 4))
    return jsonify(report_data)

if __name__ == "__main__":
    app.run(debug=True)