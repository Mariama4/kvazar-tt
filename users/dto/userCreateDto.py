from typing import TypedDict


class CreateUserDto(TypedDict):
    username: str
    email: str
