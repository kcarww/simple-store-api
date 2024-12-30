import pytest
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.product.domain.product import Product
from django_project.product.repository import DjangoORMProductRepository

@pytest.fixture
def product_created() -> Product:
    return Product(
        name='Product 1',
        description='Description of product 1',
        stock=10,
        active=True,
        price=10.0
    )

@pytest.fixture
def product_repository() -> DjangoORMProductRepository:
    return DjangoORMProductRepository()



@pytest.mark.django_db
class TestCreateProductAPI:
    def test_when_payload_is_invalid_then_return_404(self):
        url = "/api/products/"
        response = APIClient().post(
            url,
            data={
                "name": "",
                "description": "Description of product 1",
                "stock": 10,
                "active": True,
                "price": "10.0"

            }
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_when_payload_is_valid_then_return_201(self):
        url = "/api/products/"
        response = APIClient().post(
            url,
            data={
                "name": "Product 1",
                "description": "Description of product 1",
                "stock": 10,
                "active": True,
                "price": 10.0
            }
        )

        assert response.status_code == status.HTTP_201_CREATED