from typing import Type

from flask import Response
from .userServiceInterface import IUserService


class IUserController:
    userService: Type[IUserService]

    def get(self) -> Response:
        raise NotImplementedError

    def create(self) -> Response:
        raise NotImplementedError

    def getById(self, id: int) -> Response:
        raise NotImplementedError

    def updateById(self, id: int) -> Response:
        raise NotImplementedError

    def delete(self, id: int) -> Response:
        raise NotImplementedError
