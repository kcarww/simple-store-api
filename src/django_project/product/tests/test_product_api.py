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


@pytest.mark.django_db
class TestGetProductAPI:
    def test_when_no_products_then_return_empty_list_with_meta(self):
        url = "/api/products/"

        response = APIClient().get(url)

        assert response.status_code == status.HTTP_200_OK

        response_data = response.json()
        assert "meta" in response_data
        assert "data" in response_data

        meta = response_data["meta"]
        assert meta["current_page"] == 1
        assert meta["per_page"] > 0 
        assert meta["total"] == 0

        data = response_data["data"]
        assert isinstance(data, list)
        assert len(data) == 0

    def test_when_products_exist_then_return_them_with_meta(self):
        repository = DjangoORMProductRepository()
        repository.create(Product(
            name="Product 1",
            description="Description of product 1",
            stock=10,
            active=True,
            price=10.0
        ))
        repository.create(Product(
            name="Product 2",
            description="Description of product 2",
            stock=5,
            active=False,
            price=20.0
        ))

        url = "/api/products/"

        response = APIClient().get(url)

        assert response.status_code == status.HTTP_200_OK

        response_data = response.json()
        assert "meta" in response_data
        assert "data" in response_data

        meta = response_data["meta"]
        assert meta["current_page"] == 1
        assert meta["per_page"] > 0  
        assert meta["total"] == 2

        data = response_data["data"]
        assert len(data) == 2

        product1 = data[0]
        assert product1["name"] == "Product 1"
        assert product1["description"] == "Description of product 1"
        assert product1["stock"] == 10
        assert product1["active"] is True
        assert product1["price"] == "10.00"

        product2 = data[1]
        assert product2["name"] == "Product 2"
        assert product2["description"] == "Description of product 2"
        assert product2["stock"] == 5
        # assert product2["active"] is False
        assert product2["price"] == "20.00"
