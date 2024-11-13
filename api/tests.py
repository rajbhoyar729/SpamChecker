import pytest
from rest_framework.test import APIClient
from api.models import User, Contact, SpamReport

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_login(api_client):
    response = api_client.post('/api/login/', {"phone": "1234567890", "password": "password123"})
    assert response.status_code == 200
    assert "access" in response.data

@pytest.fixture
def test_user(db):
    return User.objects.create_user(name="Test User", phone="1234567890", password="password123")


@pytest.fixture
def auth_client(api_client, test_user):
    response = api_client.post('/api/login/', {'phone': test_user.phone, 'password': 'password123'})
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

def test_user_registration(api_client):
    response = api_client.post('/api/register/', {
        "name": "New User",
        "phone": "9876543210",
        "password": "password123",
        "email": "newuser@example.com"
    })
    assert response.status_code == 201
    assert "id" in response.data

def test_profile_view(auth_client, test_user):
    response = auth_client.get('/api/profile/')
    assert response.status_code == 200
    assert response.data["name"] == test_user.name

def test_add_contact(auth_client):
    response = auth_client.post('/api/contacts/', {
        "name": "Contact Name",
        "phone": "5555555555"
    })
    assert response.status_code == 201
    assert response.data["name"] == "Contact Name"

def test_mark_spam(auth_client):
    response = auth_client.post('/api/spam/', {
        "phone_number": "1111111111"
    })
    assert response.status_code == 201
    assert response.data["phone_number"] == "1111111111"

def test_search_by_name(auth_client, test_user):
    response = auth_client.get('/api/search/name/', {"name": "Test"})
    assert response.status_code == 200
    assert len(response.data) > 0

def test_search_by_phone(auth_client, test_user):
    response = auth_client.get(f'/api/search/phone/{test_user.phone}/')
    assert response.status_code == 200
    assert response.data["registered_user"]["phone"] == test_user.phone

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(name="Test User", phone="1234567890", password="password123")
    assert user.phone == "1234567890"


def test_login(api_client, test_user):
    response = api_client.post('/api/login/', {"phone": test_user.phone, "password": "password123"})
    assert response.status_code == 200
    assert "access" in response.data
