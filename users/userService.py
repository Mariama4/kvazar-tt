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
        users = self.userRepository.getAll()
        return users

    def getPaginatedUsers(self, page: int, per_page: int) -> list[UserModel]:
        users = self.userRepository.getPaginatedUsers(page, per_page)
        return users

    def create(self, data: UserModel) -> UserModel:
        user = self.userRepository.create(data)
        return user

    def getById(self, id: int) -> UserModel:
        user = self.userRepository.getById(id)
        return user

    def updateById(self, id: int, data: UserModel) -> UserModel:
        user = self.userRepository.updateById(id, data)
        return user

    def delete(self, id: int) -> bool:
        isDeleted = self.userRepository.delete(id)
        return isDeleted

    def getUserInfo(self, domain) -> dict:
        count_of_users = self.userRepository.getCountUsersRegisteredLastWeek()
        top_users_with_longest_usernames = self.userRepository.getTopLongestUsernames()
        percent_of_users = self.userRepository.getDomainEmailRatio(domain)

        return {
            "countUsersForWeek": count_of_users,
            "percentOfDomain": {
                "domain": domain,
                "percent": percent_of_users,
            },
            "topUsersWithLongestUsernames": top_users_with_longest_usernames,
        }
