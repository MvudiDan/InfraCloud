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

def create_user(username: str, password: str) -> bool:
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)", (username, hash_value))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username: str, password: str) -> bool:
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT HASH FROM USER_HASH WHERE USERNAME = ?", (username,))
    row = c.fetchone()
    conn.close()
    if not row:
        return False
    return row[0] == hashlib.sha256(password.encode()).hexdigest()

# Root gaat direct naar login
@app.route("/")
def root():
    return redirect(url_for("login"))

# LOGIN PAGE (dit is jouw PF2)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if verify_user(username, password):
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username/password.")

    return render_template("login.html", error=None)

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return f"Login success Welcome, {session['user']}"

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# Hidden API endpoint om test-users te maken 
@app.route("/signup/v2", methods=["POST"])
def signup_v2():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not username or not password:
        return "Missing username/password", 400

    if create_user(username, password):
        return "signup success", 200
    return "username has been registered.", 409


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context="adhoc")
