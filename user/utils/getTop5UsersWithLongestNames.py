from typing import Type
from ..userModel import UserModel


def get_top_5_users_with_longest_names(user_model: Type[UserModel]) -> list[UserModel]:
    """Getting the top 5 users with the longest usernames (sorted in descending order).

    :param user_model: User model representing the user object.
    :return: List of `UserModel` objects representing the users.
    """
    users = user_model.query.order_by(user_model.username.desc()).limit(5).all()
    return users
