from .main import app
from fastapi.testclient import TestClient

test_client = TestClient(app)


def test_add_pet():
    response = test_client.put(
        "/pets",
        json={
            "name": "Buddy",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    assert response.status_code == 201

    # Assert duplicates names cannot be entered

    response = test_client.put(
        "/pets",
        json={
            "name": "Buddy",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    assert response.status_code == 400
    # Assert body is validated
    response = test_client.put(
        "/pets",
        json={
            "breed": "Labrador",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    assert response.status_code == 422

    # Cleanup
    test_client.delete("/pets/Buddy")

def test_get_by_name():
    test_client.put(
        "/pets",
        json={
            "name": "Buddy",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )

    response = test_client.get("/pets/Buddy")
    assert response.status_code == 200

    response = test_client.get("pets/NotBuddy")
    assert response.status_code == 404
    # Cleanup
    test_client.delete("/pets/Buddy")


def test_get_by_type():
    test_client.put(
        "/pets",
        json={
            "name": "Buddy",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    test_client.put(
        "/pets",
        json={
            "name": "Buddy2",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    response = test_client.get("/pets?type=Dog")
    assert response.status_code == 200
    assert len(response.json()["pets"]) == 2

    response = test_client.get("/pets?type=Cat")
    assert response.status_code == 200
    assert len(response.json()["pets"]) == 0
    # Cleanup
    test_client.delete("/pets/Buddy")
    test_client.delete("/pets/Buddy2")
    
def test_delete_by_name():
    test_client.put(
        "/pets",
        json={
            "name": "Buddy",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
     
    response = test_client.delete("/pets/Buddy")
    assert response.status_code == 204
    # Should still return 204 for record that does not exist
    response = test_client.delete("/pets/Buddy2")
    assert response.status_code == 204

def test_delete_by_type():
    test_client.put(
        "/pets",
        json={
            "name": "Buddy",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    test_client.put(
        "/pets",
        json={
            "name": "Buddy2",
            "breed": "Labrador",
            "type": "Dog",
            "image": "https://images.dog.ceo/breeds/dane-great/n02109047_21903.jpg",
            "ranking": 50,
        },
    )
    response = test_client.delete("/pets?type=Dog")
    assert response.status_code == 200
    assert response.json()["rows_affected"] == 2

    response = test_client.delete("/pets?type=Cat")
    assert response.status_code == 200
    assert  response.json()["rows_affected"] == 0
    
 