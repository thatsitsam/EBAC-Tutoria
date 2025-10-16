import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.fixture
def user():
    return User.objects.create_user(username="samir", password="SenhaForte123!")

@pytest.fixture
def auth_client(user):
    client = APIClient()
    resp = client.post("/api/login/", {"username": "samir", "password": "SenhaForte123!"}, format="json")
    token = resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client

@pytest.mark.django_db
def test_list_tasks(auth_client, user):
    Task.objects.create(title="Tarefa 1", owner=user)
    resp = auth_client.get("/api/tasks/")
    assert resp.status_code == 200
    assert any(t["title"] == "Tarefa 1" for t in resp.data)

@pytest.mark.django_db
def test_create_task(auth_client):
    payload = {"title": "Nova tarefa", "description": "Detalhes", "status": "pendente"}
    resp = auth_client.post("/api/tasks/", payload, format="json")
    assert resp.status_code == 201
    assert resp.data["title"] == "Nova tarefa"

@pytest.mark.django_db
def test_retrieve_task(auth_client, user):
    task = Task.objects.create(title="Detalhar", owner=user)
    resp = auth_client.get(f"/api/tasks/{task.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "Detalhar"

@pytest.mark.django_db
def test_update_task(auth_client, user):
    task = Task.objects.create(title="Editar", owner=user, status="pendente")
    resp = auth_client.patch(f"/api/tasks/{task.id}/", {"status": "concluida"}, format="json")
    assert resp.status_code == 200
    assert resp.data["status"] == "concluida"

@pytest.mark.django_db
def test_delete_task(auth_client, user):
    task = Task.objects.create(title="Apagar", owner=user)
    resp = auth_client.delete(f"/api/tasks/{task.id}/")
    assert resp.status_code == 204
    assert not Task.objects.filter(id=task.id).exists()