from flask import Flask

from config import DevelopmentConfig, ProductionConfig
from db import db
from user import UserRouter

app = Flask(__name__)
app.config.from_object(DevelopmentConfig if app.config["DEBUG"] else ProductionConfig)
db.init_app(app)

with app.app_context():
    db.create_all()

UserRouter(app, "users")

if __name__ == "__main__":
    app.run()
