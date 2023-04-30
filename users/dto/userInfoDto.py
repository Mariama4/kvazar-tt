from typing import TypedDict

from ..userModel import UserModel


class GetInfoUsersDto(TypedDict):
    domain: str


class PercentOfDomain(TypedDict):
    domain: str
    percent: float


class InfoUsersDto(TypedDict):
    countUsersForWeek: int
    percentOfDomain: PercentOfDomain
    topUsersWithLongestUsernames: list[UserModel]
