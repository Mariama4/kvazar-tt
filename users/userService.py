from .dto import CreateUserDto, InfoUsersDto, UpdateUserDto
from .userModel import UserModel
from .userRepository import UserRepository
from .interfaces import IUserService, IUserRepository


class UserService(IUserService):
    """Represents a service for the user resource in application.

    Attributes:
        userRepository: Class representing the user model in application.
    """

    userRepository: IUserRepository = UserRepository()

    def getAll(self) -> list[UserModel]:
        users: list[UserModel] = self.userRepository.getAll()
        return users

    def getPaginatedUsers(self, page: int, per_page: int) -> list[UserModel]:
        users: list[UserModel] = self.userRepository.getPaginatedUsers(
            page=page, per_page=per_page
        )
        return users

    def create(self, data: CreateUserDto) -> UserModel:
        user: UserModel = self.userRepository.create(data=data)
        return user

    def getById(self, user_id: int) -> UserModel:
        user: UserModel = self.userRepository.getById(user_id=user_id)
        return user

    def updateById(self, user_id: int, data: UpdateUserDto) -> UserModel:
        user: UserModel = self.userRepository.updateById(user_id=user_id, data=data)
        return user

    def delete(self, user_id: int) -> bool:
        isDeleted: bool = self.userRepository.delete(user_id=user_id)
        return isDeleted

    def getUserInfo(self, domain: str) -> InfoUsersDto:
        count_of_users: int = self.userRepository.getCountUsersRegisteredLastWeek()
        top_users_with_longest_usernames: list[
            UserModel
        ] = self.userRepository.getTopLongestUsernames()
        percent_of_users: float = self.userRepository.getDomainEmailRatio(domain=domain)

        return {
            "countUsersForWeek": count_of_users,
            "percentOfDomain": {
                "domain": domain,
                "percent": percent_of_users,
            },
            "topUsersWithLongestUsernames": top_users_with_longest_usernames,
        }
