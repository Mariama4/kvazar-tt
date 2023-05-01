USER = {"username": "georgy", "email": "georgy@mail.ru"}


def test_register_user(client):
    response = client.post("/api/users", json=USER)

    assert response.status_code == 200
    assert not response.json["id"] is None
    assert response.json["username"] == USER["username"]
    assert response.json["email"] == USER["email"]
    assert not response.json["registration_date"] is None


def test_get_users(client):
    response = client.get("/api/users/")

    assert response.status_code == 200


def test_delete_user(client):
    response = client.post("/api/users", json=USER)

    assert response.status_code == 200

    response = client.delete(f"/api/users/{response.json['id']}")

    assert response.status_code == 200
    assert response.json["deleted"] is True


def test_getById_user(client):
    response = client.post("/api/users", json=USER)

    assert response.status_code == 200

    response = client.get(f"/api/users/{response.json['id']}")

    assert response.status_code == 200
    assert not response.json["id"] is None
    assert response.json["username"] == USER["username"]
    assert response.json["email"] == USER["email"]
    assert not response.json["registration_date"] is None


def test_updateById_user(client):
    response = client.post("/api/users", json=USER)

    assert response.status_code == 200

    user = {"username": "ivan", "email": "ivan@mail.ru"}

    response = client.patch(f"/api/users/{response.json['id']}", json=user)

    assert response.status_code == 200
    assert not response.json["id"] is None
    assert response.json["username"] == user["username"]
    assert response.json["email"] == user["email"]
    assert not response.json["registration_date"] is None


def test_pagination_users(client):
    response = client.post("/api/users", json=USER)

    assert response.status_code == 200

    response = client.get("/api/users?page=1&per_page=10")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_getInfo_users(client):
    response = client.post("/api/users", json=USER)

    assert response.status_code == 200

    json_data = {"domain": "georgy@mail.ru"}

    response = client.post("/api/users/info", json=json_data)

    assert response.status_code == 200
