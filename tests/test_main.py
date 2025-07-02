import pytest
from httpx import AsyncClient
from app.main import app

pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:

        # Testa o registro
        response = await ac.post("/register", json={"email": "caio@gmail.com", "password": "abc123"})
        assert response.status_code == 200

        # Testa o login
        response = await ac.post("/login", json={"email": "caio@gmail.com", "password": "abc123"})
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"