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
        """Gets all users or paginated users from application.

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
        """Creates a new user in application.

        :return: Flask `Response` object containing the JSON representation of the created user.
        """
        data = request.json
        user = self.userService.create(data)
        return jsonify(user)

    def getById(self, id: int) -> Response:
        """Gets a user with the specified ID from the application.

        :param id: The ID the user to retrieve.
        :return: Flask `Response` object containing the JSON representation of the retrieved user.
        """
        user = self.userService.getById(id)
        return jsonify(user)

    def updateById(self, id: int) -> Response:
        """Updates a user with the specified ID in application.

        :param id: The ID of the user to update.
        :return: Flask `Response` object containing the JSON representation of the updated user.
        """
        data = request.json
        user = self.userService.updateById(id, data)
        return jsonify(user)

    def delete(self, id: int) -> Response:
        ...
