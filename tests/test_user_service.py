from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.schemas.user_schema import UserCreate, UserUpdate
from app.services.user_service import UserService


def test_get_users_success():
    repository = Mock()
    repository.get_all.return_value = []

    service = UserService(repository)

    response = service.get_users()

    assert response == []
    repository.get_all.assert_called_once()


def test_get_user_by_id_success():
    user = Mock()
    repository = Mock()
    repository.get_by_id.return_value = user

    service = UserService(repository)

    response = service.get_user_by_id("user-id")

    assert response == user
    repository.get_by_id.assert_called_once_with("user-id")


def test_get_user_by_id_not_found():
    repository = Mock()
    repository.get_by_id.return_value = None

    service = UserService(repository)

    with pytest.raises(HTTPException) as exc:
        service.get_user_by_id("non-existing-id")

    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"


def test_create_user_success():
    repository = Mock()
    repository.get_by_email.return_value = None
    repository.get_by_username.return_value = None

    created_user = Mock()
    repository.create.return_value = created_user

    service = UserService(repository)

    payload = UserCreate(
        username="userTestServiceCreate",
        email="userTestServiceCreate@example.com",
        first_name="Test",
        last_name="Service",
        role="user"
    )

    response = service.create_user(payload)

    assert response == created_user
    repository.create.assert_called_once_with(payload)


def test_create_user_duplicate_email():
    repository = Mock()
    repository.get_by_email.return_value = True

    service = UserService(repository)

    payload = UserCreate(
        username="userTestService",
        email="userTestService@example.com",
        first_name="Test",
        last_name="Service",
        role="user"
    )

    with pytest.raises(HTTPException) as exc:
        service.create_user(payload)

    assert exc.value.status_code == 409
    assert exc.value.detail == "Email already exists"


def test_create_user_duplicate_username():
    repository = Mock()
    repository.get_by_email.return_value = None
    repository.get_by_username.return_value = True

    service = UserService(repository)

    payload = UserCreate(
        username="userTestService",
        email="userTestService@example.com",
        first_name="Test",
        last_name="Service",
        role="user"
    )

    with pytest.raises(HTTPException) as exc:
        service.create_user(payload)

    assert exc.value.status_code == 409
    assert exc.value.detail == "Username already exists"


def test_update_user_success():
    existing_user = Mock()
    updated_user = Mock()

    repository = Mock()
    repository.get_by_id.return_value = existing_user
    repository.update.return_value = updated_user

    service = UserService(repository)

    payload = UserUpdate(
        first_name="Updated",
        role="admin"
    )

    response = service.update_user("user-id", payload)

    assert response == updated_user
    repository.get_by_id.assert_called_once_with("user-id")
    repository.update.assert_called_once_with(existing_user, payload)

def test_update_user_not_found():
    repository = Mock()
    repository.get_by_id.return_value = None

    service = UserService(repository)

    payload = UserUpdate(
        first_name="After",
        role="admin"
    )

    with pytest.raises(HTTPException) as exc:
        service.update_user("non-existing-id", payload)

    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"

def test_update_user_duplicate_email():
    existing_user = Mock()

    repository = Mock()
    repository.get_by_id.return_value = existing_user
    repository.get_by_email.return_value = True

    service = UserService(repository)

    payload = UserUpdate(
        email="duplicated@example.com"
    )

    with pytest.raises(HTTPException) as exc:
        service.update_user("user-id", payload)

    assert exc.value.status_code == 409
    assert exc.value.detail == "Email already exists"

def test_delete_user_success():
    existing_user = Mock()

    repository = Mock()
    repository.get_by_id.return_value = existing_user

    service = UserService(repository)

    response = service.delete_user("user-id")

    assert response is None
    repository.get_by_id.assert_called_once_with("user-id")
    repository.delete.assert_called_once_with(existing_user)


def test_delete_user_not_found():
    repository = Mock()
    repository.get_by_id.return_value = None

    service = UserService(repository)

    with pytest.raises(HTTPException) as exc:
        service.delete_user("non-existing-id")

    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"

def test_update_user_duplicate_username():
    existing_user = Mock()

    repository = Mock()
    repository.get_by_id.return_value = existing_user
    repository.get_by_email.return_value = None
    repository.get_by_username.return_value = True

    service = UserService(repository)

    payload = UserUpdate(
        username="duplicatedUsername"
    )

    with pytest.raises(HTTPException) as exc:
        service.update_user("user-id", payload)

    assert exc.value.status_code == 409
    assert exc.value.detail == "Username already exists"