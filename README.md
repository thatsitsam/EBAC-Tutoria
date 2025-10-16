# EBAC-Tutoria - Projeto para teste de tutoria da EBAC.

# Task Manager API

API RESTful para gerenciamento de tarefas (To-Do System), desenvolvida em **Django 4.x** + **Django REST Framework**, com autenticação via **JWT**.

Cada usuário pode:
- Criar conta e realizar login
- Gerenciar suas próprias tarefas (criar, listar, editar, excluir)
- Visualizar apenas as tarefas associadas à sua conta

---

## Tecnologias
- Python 3.10+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (JWT)
- SQLite (padrão) ou PostgreSQL
- pytest + pytest-django (testes)

---

## Estrutura do Projeto

task_manager/ ├── manage.py ├── pytest.ini ├── requirements.txt ou pyproject.toml ├── task_manager/ │   ├── settings.py │   ├── urls.py │   └── ... ├── users/ │   ├── models.py │   ├── serializers.py │   ├── views.py │   ├── urls.py │   └── tests/ │       └── test_users.py └── tasks/ ├── models.py ├── serializers.py ├── views.py ├── urls.py └── tests/ └── test_tasks.py


---

## Instalação e Setup

# criar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# aplicar migrações
python manage.py makemigrations
python manage.py migrate

# criar superusuário (opcional)
python manage.py createsuperuser

# rodar servidor
python manage.py runserver

## Autenticação
A API usa JWT.
- POST /api/register/ → cria usuário
- POST /api/login/ → retorna access e refresh tokens
- POST /api/token/refresh/ → renova token de acesso
Exemplo de login:

POST /api/login/
Content-Type: application/json

{
  "username": "samir",
  "password": "SenhaForte123!"
}

Resposta:

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
  "access": "eyJ0eXAiOiJKV1QiLCJh..."
}

# Use o token de acesso no header:
Authorization: Bearer <access_token>

## Endpoints

# Método  Rota               Descrição
  POST    /api/register/     Cria novo usuário
  POST    /api/login/        Retorna token JWT
  GET     /api/tasks/        Lista tarefas
  POST    /api/tasks/        Cria tarefa
  GET     /api/tasks/{id}/   Detalha tarefa
  PUT     /api/tasks/{id}/   Atualiza tarefa
  PATCH   /api/tasks/{id}/   Atualiza parcialmente
  DELETE  /api/tasks/{id}/   Exclui tarefa

# Exemplo de criação de tarefa

POST /api/tasks/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Comprar pão",
  "description": "Integral",
  "status": "pendente",
  "due_date": "2025-10-20"
}

## Testes

# Rodar todos os testes:
pytest -v

# Rodar apenas os testes de tarefas:
pytest tasks/tests/ -v

# Status do projeto:

- [x] Registro e login de usuários
- [x] Autenticação JWT
- [x] CRUD de tarefas por usuário
- [x] Testes automatizados (pytest + pytest-django)


