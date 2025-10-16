import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    payload = {
        "username": "samir",
        "email": "samir@example.com",
        "password": "SenhaForte123!",
        "password_confirm": "SenhaForte123!"
    }
    resp = client.post("/api/register/", payload, format="json")
    assert resp.status_code == 201
    assert User.objects.filter(username="samir").exists()

@pytest.mark.django_db
def test_login_user():
    User.objects.create_user(username="samir", password="SenhaForte123!")
    client = APIClient()
    resp = client.post("/api/login/", {"username": "samir", "password": "SenhaForte123!"}, format="json")
    assert resp.status_code == 200
    assert "access" in resp.data
    assert "refresh" in resp.data