import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ping_google_success(client):
    """Тест: пинг google.com успешен"""
    response = client.get('/')
    assert response.status_code == 200
    assert "Пинг google.com успешен!" in response.data.decode('utf-8')

def test_ping_google_response_not_empty(client):
    """Тест: ответ не пустой"""
    response = client.get('/')
    assert len(response.data) > 0

def test_ping_google_status_code(client):
    """Тест: статус ответа 200"""
    response = client.get('/')
    assert response.status_code == 200
