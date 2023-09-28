from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import yaml
from random import shuffle

app = Flask(__name__)

with open("tailspin_scenes.yml", "r") as f:
    fragments = yaml.safe_load(f)


@app.route("/")
def index():
    title = "Tailspin"
    content = "This is a recreation of Tailspin, originally created in Flash."
    return render_template("index.html", title=title, content=content)


@app.route("/<int:scene_id>/")
def scene(scene_id):
    length = len(fragments[scene_id])
    next_scene = scene_id + 1
    keys = list(fragments[scene_id].keys())
    shuffle(keys)
    # print(keys)
    return render_template(
        "scene.html", scene_id=scene_id, keys=keys, length=length, next_scene=next_scene
    )


@app.route("/<int:scene_id>/<string:frag_id>")
def sc_frag(scene_id, frag_id):
    text = fragments[scene_id][frag_id]["text"]
    lines = text.split("\n")
    return render_template("sc_frag.html", lines=lines, frag_id=frag_id)


@app.route("/remove/<string:frag_id>")
def remove(frag_id):
    return f"{frag_id} gone"
