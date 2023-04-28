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
        """Gets all users from application.

        :return: Flask `Response` object containing the JSON representation of the users.
        """
        users = self.userService.getAll()
        return jsonify(users)

    def getPaginatedUsers(self) -> Response:
        """Getting users with pagination

        :return: Flask `Response` object containing the JSON representation of the users.
        """
        page = request.args.get("page", None, type=int)
        per_page = request.args.get("per_page", None, type=int)
        if page is None or per_page is None:
            abort(400, "Не переданы значения.")

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
        """Deletes a user with the specified ID from application.

        :param id: The ID of the user to delete.
        :return: Flask `Response` object containing the JSON representation of the result of the delete operation.
        """
        result = self.userService.delete(id)
        return jsonify(result)

    def getCountUsersForLastWeek(self) -> Response:
        """ Getting users registered per week.

        :return: Flask `Response` object containing the JSON representation of number users registered per week.
        """
        countOfUsers = self.userService.getCountUsersRegisteredLastWeek()
        return jsonify({
            "Users": countOfUsers
        })

    def getTopLongestUsernames(self) -> Response:
        """Getting the top 5 users with the longest usernames.

        :return: Flask `Response` object containing the JSON representation list of the users.
        """
        users = self.userService.getTopLongestUsernames()
        return jsonify(users)

    def getDomainEmailRatio(self, domain: str) -> Response:
        """Getting users who have a similar domain in email.

        :param domain: Email Domain (for example, "example.com").
        :return: Flask `Response` object containing the JSON representation of percentage users with similar domain.
        """
        percent = self.userService.getDomainEmailRatio(domain)
        return jsonify({domain: percent})

    def getUsersInfo(self) -> Response:
        """Getting information about users:
            - Number of users registered in the last week;
            - Top 5 users with the longest usernames;
            - Percentage of users who have an identical domain.

        :return: A Flask `Response` object containing a JSON representation of the data:\
            "countUsersForWeek": countOfUsers,\
            `domain`: percentOfUsers,\
            "topUsersWithLongestUsernames": topUsersWithLongestUsernames
        """

        data = request.json
        if not (data['domain']):
            raise abort(400, 'Нет параметра `domain`')
        domain = data['domain']

        countOfUsers = self.userService.getCountUsersRegisteredLastWeek()
        topUsersWithLongestUsernames = self.userService.getTopLongestUsernames()
        percentOfUsers = self.userService.getDomainEmailRatio(domain)

        return jsonify({
            "countUsersForWeek": countOfUsers,
            domain: percentOfUsers,
            "topUsersWithLongestUsernames": topUsersWithLongestUsernames
        })
