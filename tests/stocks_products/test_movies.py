import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_get_stock(client):
    response = client.get('/api/v1/stocks/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_product(client):
    response = client.post('/api/v1/products/',{
                                                "title": "Помидор",
                                                "description": "Лучшие помидоры на рынке"
                                                })
    assert response.status_code == 201
    assert response.data == {'title': 'Помидор', 'description': 'Лучшие помидоры на рынке'}






