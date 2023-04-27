from flask import Response
from .userServiceInterface import IUserService


class IUserController:
    userService: IUserService

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

    def getCountUsersForLastWeek(self) -> Response:
        raise NotImplementedError

    def getTopLongestUsernames(self) -> Response:
        raise NotImplementedError

    def getDomainEmailRatio(self, domain: str) -> Response:
        raise NotImplementedError
