from datetime import datetime, timedelta
from typing import Type

from ..userModel import UserModel


def get_count_users_registered_last_week(user_model: Type[UserModel]) -> int:
    """Gets the number of users registered in the last 7 days.

    :param user_model: User model representing the user object.
    :return: Number of users who signed up in the last 7 days.
    """
    last_week = datetime.utcnow() - timedelta(days=7)
    users: list[UserModel] = user_model.query.filter(
        user_model.registration_date >= last_week
    ).all()
    return len(users)
