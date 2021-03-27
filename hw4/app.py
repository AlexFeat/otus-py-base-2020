#!/usr/bin/env python3

from flask import Flask, render_template
from views.menu import v_menu


app = Flask(__name__)

app.register_blueprint(v_menu, url_prefix="/menu")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True,
    )
