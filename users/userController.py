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

    def getCountUsersForLastWeek(self) -> Response:
        countOfUsers = self.userService.getCountUsersRegisteredLastWeek()
        return jsonify({"Users": countOfUsers})

    def getTopLongestUsernames(self) -> Response:
        users = self.userService.getTopLongestUsernames()
        return jsonify(users)

    def getDomainEmailRatio(self, domain: str) -> Response:
        percent = self.userService.getDomainEmailRatio(domain)
        return jsonify({domain: percent})

    def getUsersInfo(self) -> Response:
        data = request.json
        if not (data["domain"]):
            raise abort(400, "Нет параметра `domain`")
        domain = data["domain"]

        countOfUsers = self.userService.getCountUsersRegisteredLastWeek()
        topUsersWithLongestUsernames = self.userService.getTopLongestUsernames()
        percentOfUsers = self.userService.getDomainEmailRatio(domain)

        return jsonify(
            {
                "countUsersForWeek": countOfUsers,
                "percentOfDomain": {
                    "domain": domain,
                    "percent": percentOfUsers,
                },
                "topUsersWithLongestUsernames": topUsersWithLongestUsernames,
            }
        )
