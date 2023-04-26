from typing import Type

from .userControllerInterface import IUserController


class IUserRouter:
    userController: Type[IUserController]
