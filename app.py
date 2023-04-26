from flask import Flask

from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig if app.config["DEBUG"] else ProductionConfig)

if __name__ == '__main__':
    app.run()
