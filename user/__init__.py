from typing import Final

from flask import Blueprint

from .interfaces import IUserController
from .userModel import UserModel
from .userController import UserController

__all__ = ['users_app']

userController: IUserController = UserController()

PATH_NAME: Final = 'users'

users_app = Blueprint(
    'users_app',
    __name__
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/",
    view_func=userController.get,
    methods=["GET"]
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/",
    view_func=userController.create,
    methods=["POST"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/<int:id>",
    view_func=userController.getById,
    methods=["GET"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/<int:id>",
    view_func=userController.updateById,
    methods=["PATCH"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/<int:id>",
    view_func=userController.delete,
    methods=["DELETE"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/count_users_for_last_week",
    view_func=userController.getCountUsersForLastWeek,
    methods=["GET"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/top_longest_usernames",
    view_func=userController.getTopLongestUsernames,
    methods=["GET"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/domain_like/<string:domain>",
    view_func=userController.getDomainEmailRatio,
    methods=["GET"],
)

users_app.add_url_rule(
    rule=f"/{PATH_NAME}/info",
    view_func=userController.getUsersInfo,
    methods=["GET"],
)