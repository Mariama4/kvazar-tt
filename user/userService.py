from flask import abort

from . import UserModel
from .interfaces import IUserService


class UserService(IUserService):
    """Represents a service for the user resource in application.

    Attributes:
        userModel: Class representing the user model in application.
    """
    userModel: UserModel = UserModel

    def getAll(self) -> list[UserModel]:
        """Gets all users from the database.

        :return: List of `UserModel` objects representing the users.
        """
        try:
            users = self.userModel.query.all()
        except Exception:
            abort(403, "Ошибка отправки пользователей.")
        else:
            return users

    def getPaginatedUsers(self, page: int, per_page: int) -> list[UserModel]:
        pass

    def create(self, data: UserModel) -> UserModel:
        pass

    def getById(self, id: int) -> UserModel:
        pass

    def updateById(self, id: int, data: UserModel) -> UserModel:
        pass

    def delete(self, id: int) -> bool:
        pass
