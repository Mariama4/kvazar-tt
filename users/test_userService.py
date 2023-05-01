import pytest
from unittest.mock import MagicMock
from .dto import CreateUserDto, UpdateUserDto
from .userModel import UserModel
from .userService import UserService


@pytest.fixture
def user_service():
    return UserService()


@pytest.fixture
def user_mock():
    user = UserModel(id=1, username="test", email="test@example.com")
    return user


def test_getAll(user_service, user_mock):
    user_service.userRepository.getAll = MagicMock(return_value=[user_mock])
    users = user_service.getAll()
    assert len(users) == 1
    assert users[0].username == "test"


def test_getPaginatedUsers(user_service, user_mock):
    user_service.userRepository.getPaginatedUsers = MagicMock(return_value=[user_mock])
    users = user_service.getPaginatedUsers(1, 10)
    assert len(users) == 1
    assert users[0].username == "test"


def test_create(user_service, user_mock):
    data = CreateUserDto(username="test", email="test@example.com")
    user_service.userRepository.create = MagicMock(return_value=user_mock)
    user = user_service.create(data)
    assert user.username == "test"
    assert user.email == "test@example.com"


def test_getById(user_service, user_mock):
    user_service.userRepository.getById = MagicMock(return_value=user_mock)
    user = user_service.getById(1)
    assert user.id == 1
    assert user.username == "test"


def test_updateById(user_service, user_mock):
    data = UpdateUserDto(username="updated_test")
    user_service.userRepository.updateById = MagicMock(return_value=user_mock)
    user = user_service.updateById(1, data)
    assert user.id == 1
    assert user.username == "test"


def test_delete(user_service):
    user_service.userRepository.delete = MagicMock(return_value=True)
    isDeleted = user_service.delete(1)
    assert isDeleted


def test_getUserInfo(user_service, user_mock):
    domain = "example.com"

    user_service.userRepository.getCountUsersRegisteredLastWeek = MagicMock(
        return_value=10
    )
    user_service.userRepository.getTopLongestUsernames = MagicMock(
        return_value=[user_mock]
    )
    user_service.userRepository.getDomainEmailRatio = MagicMock(return_value=50.0)

    info = user_service.getUserInfo(domain)

    assert info["countUsersForWeek"] == 10
    assert info["percentOfDomain"]["domain"] == domain
    assert info["percentOfDomain"]["percent"] == 50.0
    assert len(info["topUsersWithLongestUsernames"]) == 1
    assert info["topUsersWithLongestUsernames"][0].username == "test"
