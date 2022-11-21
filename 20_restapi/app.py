from flask import Flask, render_template, request
import request, json

app = Flask(__name__)

@app.route("/")
def render_img():
    f = open("key_nasa.txt", "r")
    api_key = f.read()
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")