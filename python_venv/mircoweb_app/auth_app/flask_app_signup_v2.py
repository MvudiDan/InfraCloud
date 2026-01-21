from flask import Flask, render_template, request
import sqlite3
import hashlib

DB_NAME = "user.db"

app = Flask(__name__)

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
    c = db.cursor()
    c.execute(
        "INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)",
        (username, pw_hash)
    )
    db.commit()
    db.close()

    return "Signup v2 success (hashed)\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5557, debug=True)
