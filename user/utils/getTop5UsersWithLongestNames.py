from typing import Type
from ..userModel import UserModel


def get_top_5_users_with_longest_names() -> list[UserModel]:
    """Getting the top 5 users with the longest usernames (sorted in descending order).

    :return: List of `UserModel` objects representing the users.
    """
    users = UserModel.query.order_by(UserModel.username.desc()).limit(5).all()
    return users
