from flask import Response

from interfaces import IUserController
from interfaces import IUserService
from .userService import UserService


class UserController(IUserController):
    """Represents a controller for the user resource in application.

    Attributes:
        userService: Service class to handle the user resource.
    """
    userService: IUserService = UserService()
    def getAll(self) -> Response: ...

    def create(self) -> Response: ...

    def getById(self, id: int) -> Response: ...

    def updateById(self, id: int) -> Response: ...

    def delete(self, id: int) -> Response: ...




