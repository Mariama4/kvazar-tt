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

        count_of_users = self.userService.getCountUsersRegisteredLastWeek()
        top_users_with_longest_usernames = self.userService.getTopLongestUsernames()
        percent_of_users = self.userService.getDomainEmailRatio(domain)

        return jsonify(
            {
                "countUsersForWeek": count_of_users,
                "percentOfDomain": {
                    "domain": domain,
                    "percent": percent_of_users,
                },
                "topUsersWithLongestUsernames": top_users_with_longest_usernames,
            }
        )
