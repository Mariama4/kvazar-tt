from flask import Flask, jsonify, Response
from config import DevelopmentConfig, ProductionConfig

from db import *
from user import *
from user.utils import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig if app.config["DEBUG"] else ProductionConfig)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/users/count_users_for_last_week', methods=['GET'])
def handler_count_users_for_last_week() -> Response:
    """An endpoint that returns the number of users registered in the last week

    :return: Flask `Response` object containing the JSON representation of number users.
    """
    countOfUsers = get_count_users_registered_last_week(UserModel)
    return jsonify({
        "Count users": countOfUsers
    })


@app.route('/users/top_longest_usernames', methods=['GET'])
def handler_top_longest_usernames() -> Response:
    """An endpoint that returns the top 5 users with the longest usernames

    :return: Flask `Response` object containing the JSON representation of number users.
    """
    users = get_top_5_users_with_longest_names(UserModel)
    return jsonify(users)


@app.route('/users/<string:domain>', methods=['GET'])
def handler_domain_email_ratio(domain: str) -> Response:
    """An endpoint that returns the percentage of users that have an identical domain among all users

    :param domain: Mail Domain (for example, "example.com").
    :return: Flask `Response` object containing the JSON representation of number users.
    """
    percent = get_domain_email_ratio(UserModel, domain)
    return jsonify({
        domain: percent
    })


if __name__ == '__main__':
    app.run()
