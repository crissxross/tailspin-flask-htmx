from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import yaml

app = Flask(__name__)

with open("tailspin_scenes.yml", "r") as f:
    fragments = yaml.safe_load(f)


@app.route("/")
def index():
    title = "Tailspin"
    content = "This is a recreation of Tailspin, originally created in Flash."
    return render_template("index.html", title=title, content=content)


@app.route("/scene1")
def scene1():
    # print(fragments[0])
    length = len(fragments[0])
    keys = list(fragments[0].keys())
    return render_template("scene1.html", keys=keys, length=length)


@app.route("/scene1/<string:frag_id>")
def sc1_frag(frag_id):
    text = fragments[0][frag_id]["text"]
    lines = text.split("\n")
    return render_template("sc1_frag.html", lines=lines)
