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
    