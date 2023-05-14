import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from logistic.models import Stock, Product


@pytest.fixture
def client():
    return APIClient()

def test():
    assert 2 == 2

@pytest.mark.django_db
def test_get_stock(client):
    response = client.get('/api/v1/stocks/')
    assert response.status_code == 300

@pytest.mark.django_db
def test_create_product(client):
    response = client.post('/api/v1/products/',{
                                                "title": "Помидор",
                                                "description": "Лучшие помидоры на рынке"
                                                })
    assert response.status_code == 201







