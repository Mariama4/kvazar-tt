from typing import Type
from flask import Flask
from .userController import UserController
from .interfaces import IUserRouter, IUserController


class UserRouter(IUserRouter):
    """Represents a router for the user endpoints in application.

    Attributes:
        userController: Controller class used to handle user business-logic.
    """

    userController: IUserController = UserController()

    def __init__(self, app: Flask, name: str) -> None:
        """Initializes the UserRouter instance.

        :param app: Flask instance representing the application.
        :param name: Name of the user resource, used in the endpoint URLs.
        """
        self.app: Flask = app
        self.name: str = name

        self.app.add_url_rule(
            rule=f"/{self.name}/", view_func=self.userController.get, methods=["GET"]
        )

        self.app.add_url_rule(
            rule=f"/{self.name}/",
            view_func=self.userController.create,
            methods=["POST"],
        )

        self.app.add_url_rule(
            rule=f"/{self.name}/<int:id>",
            view_func=self.userController.getById,
            methods=["GET"],
        )

        self.app.add_url_rule(
            rule=f"/{self.name}/<int:id>",
            view_func=self.userController.updateById,
            methods=["PATCH"],
        )

        self.app.add_url_rule(
            rule=f"/{self.name}/<int:id>",
            view_func=self.userController.delete,
            methods=["DELETE"],
        )

        self.app.add_url_rule(
            rule=f"/{self.name}/count_users_for_last_week",
            view_func=self.userController.getCountUsersForLastWeek,
            methods=["GET"],
        )

        self.app.add_url_rule(
            rule=f"/{self.name}/top_longest_usernames",
            view_func=self.userController.getTopLongestUsernames,
            methods=["GET"],
        )
