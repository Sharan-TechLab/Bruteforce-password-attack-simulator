from flask import Flask, render_template, request
import hashlib
import time

app = Flask(__name__)

CORRECT_PASSWORD = "admin123"
CORRECT_HASH = hashlib.sha256(CORRECT_PASSWORD.encode()).hexdigest()
MAX_ATTEMPTS = 5

attempts = 0
locked = False

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

            attempts += 1
            time.sleep(1)  # delay

            if password_hash == CORRECT_HASH:
                message = " Login successful!"
                attempts = 0
            elif attempts >= MAX_ATTEMPTS:
                locked = True
                message = " Account locked"
            else:
                message = f" Wrong password (Attempt {attempts})"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
