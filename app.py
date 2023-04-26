from flask import Flask

from config import DevelopmentConfig, ProductionConfig
from db import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig if app.config["DEBUG"] else ProductionConfig)
db.init_app(app)

if __name__ == '__main__':
    app.run()
