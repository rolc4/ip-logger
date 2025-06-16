from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_ip():
    ip = request.remote_addr
    data = request.form.to_dict()
    with open("ips.txt", "a") as f:
        f.write(f"{datetime.now()} - {ip} - {data}\n")
    return "Logged", 200

@app.route('/')
def home():
    return "IP Logger is running!", 200
