from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_user_success():
    payload = {
        "username": "userTestDev",
        "email": "userTestDev@example.com",
        "first_name": "Test",
        "last_name": "Dev",
        "role": "user"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["role"] == payload["role"]
    assert data["active"] is True
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_create_user_duplicate_email():
    payload = {
        "username": "userTestQA",
        "email": "userTestQA@example.com",
        "first_name": "Test",
        "last_name": "QA",
        "role": "user"
    }

    first_response = client.post("/users", json=payload)

    assert first_response.status_code == 201

    duplicate_payload = {
        "username": "userTestQADuplicate",
        "email": "userTestQA@example.com",
        "first_name": "Test",
        "last_name": "QA",
        "role": "admin"
    }

    response = client.post("/users", json=duplicate_payload)

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already exists"


def test_get_users_success():
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id_not_found():
    response = client.get("/users/non-existing-id")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_update_user_success():
    create_payload = {
        "username": "userTestUpdate",
        "email": "userTestUpdate@example.com",
        "first_name": "Before",
        "last_name": "Update",
        "role": "user"
    }

    create_response = client.post("/users", json=create_payload)
    assert create_response.status_code == 201

    user = create_response.json()

    update_payload = {
        "first_name": "After",
        "role": "admin"
    }

    response = client.patch(
        f"/users/{user['id']}",
        json=update_payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["first_name"] == "After"
    assert data["role"] == "admin"


def test_delete_user_success():
    create_payload = {
        "username": "userTestDelete",
        "email": "userTestDelete@example.com",
        "first_name": "Delete",
        "last_name": "User",
        "role": "guest"
    }

    create_response = client.post("/users", json=create_payload)
    assert create_response.status_code == 201

    user = create_response.json()

    response = client.delete(f"/users/{user['id']}")

    assert response.status_code == 204

    get_response = client.get(f"/users/{user['id']}")

    assert get_response.status_code == 404