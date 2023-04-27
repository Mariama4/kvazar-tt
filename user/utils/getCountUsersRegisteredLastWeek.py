from datetime import datetime, timedelta
from ..userModel import UserModel


def get_count_users_registered_last_week() -> int:
    """Gets the number of users registered in the last 7 days.

    :return: Number of users who signed up in the last 7 days.
    """
    last_week = datetime.utcnow() - timedelta(days=7)
    users: list[UserModel] = UserModel.query.filter(
        UserModel.registration_date >= last_week
    ).all()
    return len(users)
