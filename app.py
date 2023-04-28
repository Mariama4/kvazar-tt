from flask import Flask
from db import db
from config import DevelopmentConfig, ProductionConfig
from users import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig if app.config["DEBUG"] else ProductionConfig)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(users_app)

if __name__ == "__main__":
    app.run()
