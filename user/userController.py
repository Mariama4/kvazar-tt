from flask import request, Response, jsonify

from interfaces import IUserController
from interfaces import IUserService
from .userService import UserService


class UserController(IUserController):
    """Represents a controller for the user resource in application.

    Attributes:
        userService: Service class used to handle the user resource.
    """
    userService: IUserService = UserService()

    def getAll(self) -> Response:
        """Gets all users or paginated users from database.

        :return: Flask `Response` object containing the JSON representation of the users.
        """
        page = request.args.get("page", None, type=int)
        per_page = request.args.get("per_page", None, type=int)

        if page is None or per_page is None:
            users = self.userService.getAll()
        else:
            users = self.userService.getPaginatedUsers(page, per_page)

        return jsonify(users)

    def create(self) -> Response:
        ...

    def getById(self, id: int) -> Response:
        ...

    def updateById(self, id: int) -> Response:
        ...

    def delete(self, id: int) -> Response:
        ...
