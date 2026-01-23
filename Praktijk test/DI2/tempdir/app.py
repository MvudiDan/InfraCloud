from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>DI2 Docker Web App</h1>
    <p>Container hostname: {hostname}</p>
    <p>Status: Running successfully</p>
    """

app.run(host="0.0.0.0", port=8080, threaded=False)
