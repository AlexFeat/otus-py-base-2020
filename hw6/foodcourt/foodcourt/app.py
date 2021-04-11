from flask import Flask, render_template
from flask_migrate import Migrate
from views.menu import v_menu
from models.database import db

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(v_menu, url_prefix="/menu")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
