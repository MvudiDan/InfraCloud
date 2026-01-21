from flask import Flask
import sqlite3

DB_NAME = "user.db"

app = Flask(__name__)

def create_tables():
    db = sqlite3.connect(DB_NAME)
    c = db.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS USER_PLAIN (
        USERNAME TEXT PRIMARY KEY NOT NULL,
        PASSWORD TEXT NOT NULL
    );
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS USER_HASH (
        USERNAME TEXT PRIMARY KEY NOT NULL,
        HASH TEXT NOT NULL
    );
    """)

    db.commit()
    db.close()


@app.route("/init", methods=["GET"])
def init_db():
    create_tables()
    return "Tables created\n", 200


@app.route("/delete/all", methods=["GET"])
def delete_all():
    create_tables()
    db = sqlite3.connect(DB_NAME)
    c = db.cursor()
    c.execute("DELETE FROM USER_PLAIN;")
    c.execute("DELETE FROM USER_HASH;")
    db.commit()
    db.close()
    return "All users deleted\n", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5599)
