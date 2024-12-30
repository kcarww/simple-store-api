import pytest

from core.product.domain.product import Product
from django_project.product.repository import DjangoORMProductRepository
from django_project.product.models import Product as ProductModel


@pytest.mark.django_db
class TestSave:
    def test_save_product_in_database(self):
        product = Product(
            name="Product 1",
            price=10.5,
            description="Description of product 1",
            stock=10
        )

        repository = DjangoORMProductRepository()
        assert ProductModel.objects.count() == 0
        repository.create(product)
        assert ProductModel.objects.count() == 1
        product_model = ProductModel.objects.first()
        assert product_model.name == "Product 1"
        assert product_model.price == 10.5
        assert product_model.description == "Description of product 1"
        assert product_model.stock == 10


@pytest.mark.django_db
class TestFindAll:
    def test_find_all_products_in_database(self):
        product_1 = Product(
            name="Product 1",
            price=10.5,
            description="Description of product 1",
            stock=10
        )

        product_2 = Product(
            name="Product 2",
            price=20.0,
            description="Description of product 2",
            stock=5

        )

        repository = DjangoORMProductRepository()
        repository.create(product_1)
        repository.create(product_2)

        products = repository.find_all()

        assert len(products) == 2

        product1 = products[0]
        assert product1.name == "Product 1"
        assert product1.price == 10.5
        assert product1.description == "Description of product 1"
        assert product1.stock == 10

        product2 = products[1]
        assert product2.name == "Product 2"
        assert product2.price == 20.0
        assert product2.description == "Description of product 2"
        assert product2.stock == 5
