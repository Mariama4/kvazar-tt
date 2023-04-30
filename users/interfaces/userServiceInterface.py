from ..dto import CreateUserDto
from ..dto import UpdateUserDto
from ..dto import InfoUsersDto
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
    def create(self, data: CreateUserDto) -> UserModel:
        """Creates a new user in the user repository.

        :param data: Dict containing the data for the new user.
        :return: The `UserModel` object representing the created user.
        """
        raise NotImplementedError

    @abstractmethod
    def getById(self, user_id: int) -> UserModel:
        """Gets a user with the specified ID from the user repository.

        :param user_id: The ID of the user to retrieve.
        :return: The `UserModel` object representing the retrieved user.
        """
        raise NotImplementedError

    @abstractmethod
    def updateById(self, user_id: int, data: UpdateUserDto) -> UserModel:
        """Updates a user with the specified ID in the user repository.

        :param user_id: The ID of the user to update.
        :param data: Dict containing the updated data for the user.
        :return: The `UserModel` object representing the updated user.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """Deletes a user with the specified ID from the user repository.

        :param user_id: The ID of the user to delete.
        :return: True if the user was successfully deleted.
        """
        raise NotImplementedError

    @abstractmethod
    def getUserInfo(self, domain: str) -> InfoUsersDto:
        """Getting information about users:
            - Number of users registered in the last week;
            - Top 5 users with the longest usernames;
            - Percentage of users who have an identical domain.

        :param domain: Email domain
        :return: return a dict
        """
        raise NotImplementedError
