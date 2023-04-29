from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from db import db
from users import *


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
    API_URL = "/static/swagger.json"  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={"app_name": __name__},  # Swagger UI config overrides
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(swagger_ui_blueprint)
    app.register_blueprint(users_app)

    return app


if __name__ == "__main__":
    from config import DevelopmentConfig

    user_app = create_app(DevelopmentConfig)
    user_app.run()
