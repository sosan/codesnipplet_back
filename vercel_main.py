from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=["get"])
def home():
    return Response("vercel")
