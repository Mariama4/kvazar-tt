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

    def __init__(self, app: Type[Flask], name: str) -> None:
        """Initializes the UserRouter instance.

        :param app: Flask instance representing the application.
        :param name: Name of the user resource, used in the endpoint URLs.
        """
        self.app: Type[Flask] = app
        self.name: str = name
