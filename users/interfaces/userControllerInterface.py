from flask import Response
from .userServiceInterface import IUserService
from abc import ABC, abstractmethod


class IUserController(ABC):
    userService: IUserService

    @abstractmethod
    def getUsers(self) -> Response:
        """Gets all users from application.

        :return: Flask `Response` object containing the JSON representation of the users.
        """
        raise NotImplementedError

    @abstractmethod
    def getPaginatedUsers(self) -> Response:
        """Getting users with pagination

        :return: Flask `Response` object containing the JSON representation of the users.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self) -> Response:
        """Creates a new user in application.

        :return: Flask `Response` object containing the JSON representation of the created user.
        """
        raise NotImplementedError

    @abstractmethod
    def getById(self, id: int) -> Response:
        """Gets a user with the specified ID from the application.

        :param id: The ID the user to retrieve.
        :return: Flask `Response` object containing the JSON representation of the retrieved user.
        """
        raise NotImplementedError

    @abstractmethod
    def updateById(self, id: int) -> Response:
        """Updates a user with the specified ID in application.

        :param id: The ID of the user to update.
        :return: Flask `Response` object containing the JSON representation of the updated user.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> Response:
        """Deletes a user with the specified ID from application.

        :param id: The ID of the user to delete.
        :return: Flask `Response` object containing the JSON representation of the result of the delete operation.
        """
        raise NotImplementedError

    @abstractmethod
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
        raise NotImplementedError
