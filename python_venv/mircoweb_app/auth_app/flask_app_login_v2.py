from flask import Flask, render_template, request
import sqlite3
import hashlib

DB_NAME = "user.db"

app = Flask(__name__)

@app.route("/login/v2", methods=["GET", "POST"])
def login_v2():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Missing username or password\n", 400

    pw_hash = hashlib.sha256(password.encode()).hexdigest()

    db = sqlite3.connect(DB_NAME)
    c = db.cursor()
    c.execute("SELECT HASH FROM USER_HASH WHERE USERNAME = ?", (username,))
    row = c.fetchone()
    db.close()

    if row and row[0] == pw_hash:
        return "Login success (hashed)\n", 200

    return "Invalid username/password\n", 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556, debug=True) 