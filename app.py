from flask import Flask, render_template, request, jsonify
import hashlib
import time
import logging
import random
from datetime import datetime

app = Flask(__name__)

CORRECT_PASSWORD = "admin123"
CORRECT_HASH = hashlib.sha256(CORRECT_PASSWORD.encode()).hexdigest()
MAX_ATTEMPTS = 5

attempts = 0
locked = False
attack_logs = []

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_ip():
    """Simulate a random IP address."""
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

@app.route("/", methods=["GET", "POST"])
def login():
    global attempts, locked

    message = ""

    if request.method == "POST":
        if locked:
            message = " Account locked due to too many attempts"
        else:
            password = request.form["password"]
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            ip = simulate_ip()

            attempts += 1
            time.sleep(1)  # delay

            log_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ip": ip,
                "attempt": attempts,
                "password": password,
                "success": False
            }

            if password_hash == CORRECT_HASH:
                message = " Login successful!"
                attempts = 0
                locked = False
                log_entry["success"] = True
            elif attempts >= MAX_ATTEMPTS:
                locked = True
                message = " Account locked"
            else:
                message = f" Wrong password (Attempt {attempts})"

            attack_logs.append(log_entry)
            logging.info(f"Login attempt from IP {ip}: Attempt {attempts}, Password: {password}, Success: {log_entry['success']}")

    return render_template("login.html", message=message, logs=attack_logs[-10:])  # Show last 10 logs

@app.route("/attack", methods=["GET", "POST"])
def attack():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        username = request.form["username"]
        # Load passwords from file
        try:
            with open("password.txt", "r") as f:
                passwords = [line.strip() for line in f]
        except FileNotFoundError:
            result = "Password file not found."
            return render_template("attack.html", result=result)

        # Simulate attack (for demo only)
        for password in passwords:
            ip = simulate_ip()
            logging.info(f"Brute force attempt from IP {ip}: URL {url}, User {username}, Password {password}")
            time.sleep(0.5)  # Simulate delay
            if password == CORRECT_PASSWORD:
                result = f"Password cracked: {password}"
                break
        else:
            result = "No password found in list."

    return render_template("attack.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
