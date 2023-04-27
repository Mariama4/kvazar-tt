from typing import Type
from ..userModel import UserModel


class IUserService:
    userModel: Type[UserModel]

    def getAll(self) -> list[UserModel]:
        raise NotImplementedError

    def getPaginatedUsers(self, page: int, per_page: int) -> list[UserModel]:
        raise NotImplementedError

    def create(self, data: UserModel) -> UserModel:
        raise NotImplementedError

    def getById(self, id: int) -> UserModel:
        raise NotImplementedError

    def updateById(self, id: int, data: UserModel) -> UserModel:
        raise NotImplementedError

    def delete(self, id: int) -> bool:
        raise NotImplementedError

    def getCountUsersForLastWeek(self) -> int:
        raise NotImplementedError

    def getTopLongestUsernames(self) -> list[UserModel]:
        raise NotImplementedError

    def getDomainEmailRatio(self, domain: str) -> float:
        raise NotImplementedError
