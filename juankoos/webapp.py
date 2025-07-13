"""Minimal Flask application for JuankoOS."""

from flask import Flask, render_template, request

from .core import JuankoOS

app = Flask(__name__)
os_instance = JuankoOS()


@app.route("/", methods=["GET", "POST"])
def index():
    lyrics = slogan = ritual = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "misterio")
        lyrics = os_instance.lyrics(prompt)
        slogan = os_instance.slogan(prompt)
        ritual = os_instance.ritual(prompt)
    return render_template("index.html", lyrics=lyrics, slogan=slogan, ritual=ritual)


def run():
    app.run(debug=True)


if __name__ == "__main__":
    run()
