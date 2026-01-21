from flask import Flask, render_template, request
import sqlite3
import hashlib

DB_NAME = "user.db"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup/v2", methods=["GET", "POST"])
def signup_v2():
    if request.method == "GET":
        return render_template("signup.html")

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Missing username or password\n", 400

    pw_hash = hashlib.sha256(password.encode()).hexdigest()

    db = sqlite3.connect(DB_NAME)
    try:
        c = db.cursor()
        c.execute(
            "INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)",
            (username, pw_hash)
        )
        db.commit()
        return "Signup success (hashed)\n", 200
    except sqlite3.IntegrityError:
        return "Username already exists\n", 409
    finally:
        db.close()

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
    

@app.route("/update/password", methods=["GET", "POST"])
def update_password():
    if request.method == "GET":
        return render_template("update_password.html")

    username = request.form.get("username")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")

    if not username or not old_password or not new_password:
        return "Missing fields\n", 400

    old_hash = hashlib.sha256(old_password.encode()).hexdigest()
    new_hash = hashlib.sha256(new_password.encode()).hexdigest()

    db = sqlite3.connect(DB_NAME)
    c = db.cursor()

    c.execute(
        "SELECT HASH FROM USER_HASH WHERE USERNAME = ?",
        (username,)
    )
    row = c.fetchone()

    if not row or row[0] != old_hash:
        db.close()
        return "Invalid username or password\n", 401

    c.execute(
        "UPDATE USER_HASH SET HASH = ? WHERE USERNAME = ?",
        (new_hash, username)
    )
    db.commit()
    db.close()

    return "Password updated successfully\n", 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True, ssl_context="adhoc")
