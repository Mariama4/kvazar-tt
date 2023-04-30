from typing import Type
from ..userModel import UserModel
from abc import ABC, abstractmethod


class IUserService(ABC):
    userModel: Type[UserModel]

    @abstractmethod
    def getAll(self) -> list[UserModel]:
        """Gets all users from the database.

        :return: List of `UserModel` objects representing the users.
        """
        raise NotImplementedError

    @abstractmethod
    def getPaginatedUsers(self, page: int, per_page: int) -> list[UserModel]:
        """Gets paginated users from the database.

        :param page: The page number of the paginated users.
        :param per_page: The number of users per page in the paginated results.
        :return: List of `UserModel` objects representing the paginated users.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self, data: UserModel) -> UserModel:
        """Creates a new user in the database.

        :param data: Dict containing the data for the new user.
        :return: The `UserModel` object representing the created user.
        """
        raise NotImplementedError

    @abstractmethod
    def getById(self, id: int) -> UserModel:
        """Gets a user with the specified ID from the database.

        :param id: The ID of the user to retrieve.
        :return: The `UserModel` object representing the retrieved user.
        """
        raise NotImplementedError

    @abstractmethod
    def updateById(self, id: int, data: UserModel) -> UserModel:
        """Updates a user with the specified ID in the database.

        :param id: The ID of the user to update.
        :param data: Dict containing the updated data for the user.
        :return: The `UserModel` object representing the updated user.
        """
        raise NotImplementedError

    def delete(self, id: int) -> bool:
        """Deletes a user with the specified ID from the database.

        :param id: The ID of the user to delete.
        :return: True if the user was successfully deleted.
        """
        raise NotImplementedError

    @abstractmethod
    def getCountUsersRegisteredLastWeek(self) -> int:
        """Getting users registered per week.

        :return: Number of users registered per week.
        """
        raise NotImplementedError

    @abstractmethod
    def getTopLongestUsernames(self) -> list[UserModel]:
        """Getting the top 5 users with the longest usernames.

        :return: List of `UserModel` objects representing top 5 users.
        """
        raise NotImplementedError

    @abstractmethod
    def getDomainEmailRatio(self, domain: str) -> float:
        """Getting users who have a similar domain in email.

        :param domain: Email Domain (for example, "example.com").
        :return: The percentage of users who have a similar percentage among all.
        """
        raise NotImplementedError
