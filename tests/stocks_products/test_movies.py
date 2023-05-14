import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from logistic.models import Stock, Product


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def make_product():
    def products(*args,**kwargs):
        return baker.make(Product,*args, **kwargs)
    
    return products

@pytest.fixture
def make_stock():
    def stocks(*args,**kwargs):
        return baker.make(Stock,*args, **kwargs)
    
    return stocks

def test():
    assert 2 == 2

# @pytest.mark.django_db
# def test_get_stock(client):
#     response = client.get('/api/v1/stocks/')
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_create_stock(client):
#     response = client.post('/api/v1/stocks/',{
#                                                 "address": "мой адрес не дом и не улица, мой адрес сегодня такой: www.ленинград-спб.ru6",
#                                                 "positions": [
#                                                     {
#                                                     "product": 4,
#                                                     "quantity": 250,
#                                                     "price": 120.50
#                                                     },
#                                                     {
#                                                     "product": 3,
#                                                     "quantity": 100,
#                                                     "price": 180
#                                                     }
#                                                 ]
#                                             })
#     assert response.status_code == 201







