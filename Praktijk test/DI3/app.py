from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    client_ip = request.remote_addr
    return render_template(
        "index.html",
        app_name="DI3 Docker Web App (Templates)",
        hostname=hostname,
        client_ip=client_ip
    )

app.run(host="0.0.0.0", port=8080, threaded=False)
