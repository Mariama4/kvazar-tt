from typing import Type

from flask import abort

from .userModel import UserModel
from .userModel import db
from .interfaces import IUserService
from .utils import get_count_users_registered_last_week, get_top_5_users_with_longest_names


class UserService(IUserService):
    """Represents a service for the user resource in application.

    Attributes:
        userModel: Class representing the user model in application.
    """

    userModel: Type[UserModel] = UserModel

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
        """Gets paginated users from the database.

        :param page: The page number of the paginated users.
        :param per_page: The number of users per page in the paginated results.
        :return: List of `UserModel` objects representing the paginated users.
        """
        users_query = self.userModel.query.paginate(page=page, per_page=per_page)
        try:
            users = users_query.items
        except Exception:
            abort(403, "Ошибка отправки пользователей")
        else:
            return users

    def create(self, data: UserModel) -> UserModel:
        """Creates a new user in the database.

        :param data: Dict containing the data for the new user.
        :return: The `UserModel` object representing the created user.
        """
        try:
            user = self.userModel(username=data["username"], email=data["email"])

            db.session.add(user)
            db.session.commit()
        except Exception:
            abort(403, "Ошибка создания пользователя")
        else:
            return user

    def getById(self, id: int) -> UserModel:
        """Gets a user with the specified ID from the database.

        :param id: The ID of the user to retrieve.
        :return: The `UserModel` object representing the retrieved user.
        """
        user = self.userModel.query.get_or_404(id)
        return user

    def updateById(self, id: int, data: UserModel) -> UserModel:
        """Updates a user with the specified ID in the database.

        :param id: The ID of the user to update.
        :param data: Dict containing the updated data for the user.
        :return: The `UserModel` object representing the updated user.
        """
        user = self.userModel.query.get_or_404(id)
        try:
            user.username = data["username"]
            user.email = data["email"]

            db.session.commit()
        except Exception:
            abort(403, "Ошибка обновления пользователя")
        else:
            return user

    def delete(self, id: int) -> bool:
        """Deletes a user with the specified ID from the database.

        :param id: The ID of the user to delete.
        :return: True if the user was successfully deleted.
        """
        user = self.userModel.query.get_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception:
            abort(403, "Ошибка удаления пользователя")
        else:
            return True

    def getCountUsersForLastWeek(self) -> int:
        """Getting users registered per week

        :return: Number of users registered per week
        """
        try:
            countOfUsers = get_count_users_registered_last_week()
        except Exception:
            abort(403, "Ошибка отправки данных о количестве пользователей за последнюю неделю")
        else:
            return countOfUsers

    def getTopLongestUsernames(self) -> list[UserModel]:
        """Getting the top 5 users with the longest usernames

        :return: List of `UserModel` objects representing top 5 users.
        """
        try:
            users = get_top_5_users_with_longest_names()
        except Exception:
            abort(403, "Ошибка отправки данных о топ 5 пользователей с самими длинными именами")
        else:
            return users
