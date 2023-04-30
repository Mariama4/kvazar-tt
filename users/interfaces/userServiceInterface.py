from ..userModel import UserModel
from .userRepositoryInterface import IUserRepository
from abc import ABC, abstractmethod


class IUserService(ABC):
    userRepository: IUserRepository

    @abstractmethod
    def getAll(self) -> list[UserModel]:
        """Gets all users from the user repository.

        :return: List of `UserModel` objects representing the users.
        """
        raise NotImplementedError

    @abstractmethod
    def getPaginatedUsers(self, page: int, per_page: int) -> list[UserModel]:
        """Gets paginated users from the user repository.

        :param page: The page number of the paginated users.
        :param per_page: The number of users per page in the paginated results.
        :return: List of `UserModel` objects representing the paginated users.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self, data: UserModel) -> UserModel:
        """Creates a new user in the user repository.

        :param data: Dict containing the data for the new user.
        :return: The `UserModel` object representing the created user.
        """
        raise NotImplementedError

    @abstractmethod
    def getById(self, id: int) -> UserModel:
        """Gets a user with the specified ID from the user repository.

        :param id: The ID of the user to retrieve.
        :return: The `UserModel` object representing the retrieved user.
        """
        raise NotImplementedError

    @abstractmethod
    def updateById(self, id: int, data: UserModel) -> UserModel:
        """Updates a user with the specified ID in the user repository.

        :param id: The ID of the user to update.
        :param data: Dict containing the updated data for the user.
        :return: The `UserModel` object representing the updated user.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> bool:
        """Deletes a user with the specified ID from the user repository.

        :param id: The ID of the user to delete.
        :return: True if the user was successfully deleted.
        """
        raise NotImplementedError

    @abstractmethod
    def getUserInfo(self, data) -> dict:
        """Getting information about users:
            - Number of users registered in the last week;
            - Top 5 users with the longest usernames;
            - Percentage of users who have an identical domain.

        :param data: JSON object that contains the domain field
        :return: return a dict
        """
        raise NotImplementedError
