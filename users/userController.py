from flask import request, Response, jsonify, abort

from . import UserModel
from .dto import InfoUsersDto, GetInfoUsersDto, CreateUserDto, UpdateUserDto
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
        users: list[UserModel] = self.userService.getAll()
        return jsonify(users)

    def getPaginatedUsers(self) -> Response:
        page = request.args.get("page", None, type=int)
        per_page = request.args.get("per_page", None, type=int)
        if page is None or per_page is None:
            abort(400, "Не переданы значения.")

        users: list[UserModel] = self.userService.getPaginatedUsers(page=page, per_page=per_page)
        return jsonify(users)

    def create(self) -> Response:
        data: CreateUserDto = request.json
        user: UserModel = self.userService.create(data)
        return jsonify(user)

    def getById(self, user_id: int) -> Response:
        user: UserModel = self.userService.getById(user_id=user_id)
        return jsonify(user)

    def updateById(self, user_id: int) -> Response:
        data: UpdateUserDto = request.json
        user: UserModel = self.userService.updateById(user_id=user_id, data=data)
        return jsonify(user)

    def delete(self, user_id: int) -> Response:
        result = self.userService.delete(user_id)
        return jsonify({"deleted": result})

    def getUsersInfo(self) -> Response:
        data: GetInfoUsersDto = request.json
        if not (data["domain"]):
            raise abort(400, "Нет параметра `domain`")
        domain = data["domain"]
        users_info: InfoUsersDto = self.userService.getUserInfo(domain=domain)
        return jsonify(users_info)
