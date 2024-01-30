# test_autenticacion.py

import pytest
# from modules.auth.models.User import User
# from user_service import UserService
# from models import User, UserService
from modules.auth.models.User import User, UserService
from database.db import db


def test_successful_login(user_service):
    # Agrega un usuario de prueba
    # user_service.create_user("testuser", "password123")

    # Intenta autenticar con las credenciales correctas
    result = user_service.authenticate_user("testuser", "password123")
    assert result is True

def test_unsuccessful_login(user_service):
    # Intenta autenticar con credenciales incorrectas
    result = user_service.authenticate_user("nonexistentuser", "wrongpassword")
    assert result is False