from datetime import datetime, timedelta
from typing import Type
from flask import abort
from .userModel import UserModel
from .userModel import db
from .interfaces import IUserService


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
        user = self.userModel.query.get_or_404(id, description="Такого пользователя нет")
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

    def getCountUsersRegisteredLastWeek(self) -> int:
        """Getting users registered per week.

        :return: Number of users registered per week.
        """
        try:
            last_week = datetime.utcnow() - timedelta(days=7)
            users = self.userModel.query.filter(
                self.userModel.registration_date >= last_week
            ).all()
        except Exception:
            abort(403, "Ошибка отправки данных о количестве пользователей за последнюю неделю")
        else:
            return len(users)

    def getTopLongestUsernames(self) -> list[UserModel]:
        """Getting the top 5 users with the longest usernames.

        :return: List of `UserModel` objects representing top 5 users.
        """
        try:
            users = self.userModel.query.order_by(self.userModel.username.desc()).limit(5).all()
        except Exception:
            abort(403, "Ошибка отправки данных о топ 5 пользователей с самими длинными именами")
        else:
            return users

    def getDomainEmailRatio(self, domain: str) -> float:
        """Getting users who have a similar domain in email.

        :param domain: Email Domain (for example, "example.com").
        :return: The percentage of users who have a similar percentage among all.
        """
        try:
            total_users = self.userModel.query.count()
            domain_users = self.userModel.query.filter(self.userModel.email.like(f"%@{domain}")).count()
            if total_users == 0:
                percent = 0.0
            else:
                percent = round((domain_users / total_users) * 100, 2)
        except Exception:
            abort(403, "Ошибка отправки данных о пользователях, у которых схожий домен")
        else:
            return percent
