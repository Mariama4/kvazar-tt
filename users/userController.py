from flask import request, Response, jsonify, abort
from .interfaces import IUserController
from .interfaces import IUserService
from .userService import UserService


class UserController(IUserController):
    """Represents a controller for the user resource in application.

    Attributes:
        userService: Service class used to handle the user resource.
    """

    userService: IUserService = UserService()

    def getUsers(self) -> Response:
        users = self.userService.getAll()
        return jsonify(users)

    def getPaginatedUsers(self) -> Response:
        page = request.args.get("page", None, type=int)
        per_page = request.args.get("per_page", None, type=int)
        if page is None or per_page is None:
            abort(400, "Не переданы значения.")

        users = self.userService.getPaginatedUsers(page, per_page)
        return jsonify(users)

    def create(self) -> Response:
        data = request.json
        user = self.userService.create(data)
        return jsonify(user)

    def getById(self, id: int) -> Response:
        user = self.userService.getById(id)
        return jsonify(user)

    def updateById(self, id: int) -> Response:
        data = request.json
        user = self.userService.updateById(id, data)
        return jsonify(user)

    def delete(self, id: int) -> Response:
        result = self.userService.delete(id)
        return jsonify({"deleted": result})

    def getUsersInfo(self) -> Response:
        data = request.json
        if not (data["domain"]):
            raise abort(400, "Нет параметра `domain`")
        domain = data["domain"]
        users_info = self.userService.getUserInfo(domain)
        return jsonify(users_info)
