import pytest
from blogApp.app import app
from fastapi.testclient import TestClient
from fastapi import status

@pytest.fixture
def usr():
    
    return {"username":"admin", "password":"admin"}
@pytest.fixture
def wrong_creditials():
     return {"username":"abcdefg", "password":"123456"}

@pytest.fixture
def client():
   return TestClient(app)

def test_routes_get_not_available(client:TestClient):
    
    response = client.get("/users")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    
def test_user_routes_valid_creditials(usr, client:TestClient):
    
    response = client.post("/users", data=usr, auth=(usr["username"],usr["password"]))
    assert response.status_code == status.HTTP_200_OK
    
def test_user_routes_invalid_creditials(wrong_creditials, client:TestClient):
    
    response = client.post("/users", data=wrong_creditials)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    