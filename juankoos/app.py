"""Minimal Flask app to interact with JuankoOS."""

from flask import Flask, render_template, request, jsonify
from .content import generate_lyrics, generate_slogan, generate_ritual

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json or {}
    action = data.get("action")
    text = data.get("text", "")
    if action == "lyrics":
        result = generate_lyrics(text)
    elif action == "slogan":
        result = generate_slogan(text)
    elif action == "ritual":
        result = generate_ritual(text)
    else:
        return jsonify({"error": "Invalid action"}), 400
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
