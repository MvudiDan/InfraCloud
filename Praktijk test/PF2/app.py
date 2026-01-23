import sqlite3
import hashlib
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "pf2-secret"
db_name = "test.db"

def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
                 (USERNAME TEXT PRIMARY KEY NOT NULL,
                  HASH TEXT NOT NULL);''')
    conn.commit()
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute(
            "INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)",
            (username, hash_value)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT HASH FROM USER_HASH WHERE USERNAME = ?", (username,))
    row = c.fetchone()
    conn.close()
    if not row:
        return False
    return row[0] == hashlib.sha256(password.encode()).hexdigest()

@app.route("/")
def root():
    return redirect(url_for("login"))

# 🔹 SIGNUP PAGE (HTML)
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if create_user(username, password):
            return redirect(url_for("login"))
        else:
            return render_template("signup.html", error="Username bestaat al")

    return render_template("signup.html", error=None)

# 🔹 LOGIN PAGE (HTML)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if verify_user(request.form["username"], request.form["password"]):
            session["user"] = request.form["username"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username/password")

    return render_template("login.html", error=None)

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
