import uuid
import pytest

from src.core.product.domain.product import Product

class TestProduct:
    def test_name_is_required(self):
        with pytest.raises(
            TypeError, match="Name cannot be empty"
        ):
            Product(
                name="",
                price=10.0,
                description="description",
                stock=10
            )

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(
            TypeError, match="Name cannot be longer than 255 characters"
        ):
            Product(
                name="a" * 256,
                price=10.0,
                description="description",
                stock=10
            )

    def test_price_must_be_positive(self):
        with pytest.raises(
            TypeError, match="Price cannot be negative"
        ):
            Product(
                name="name",
                price=-10.0,
                description="description",
                stock=10
            )

    def test_description_must_have_less_than_255_characters(self):
        with pytest.raises(
            TypeError, match="Description cannot be longer than 255 characters"
        ):
            Product(
                name="name",
                price=10.0,
                description="a" * 256,
                stock=10
            )

    def test_activate(self):
        product = Product(
            name="name",
            price=10.0,
            description="description",
            stock=10
        )

        product.deactivate()
        assert not product.active

        product.activate()
        assert product.active

    def test_create_product(self):
        product = Product(
            name="name",
            price=10.0,
            description="description",
            stock=10
        )

        assert product.id
        assert product.name == "name"
        assert product.price == 10.0
        assert product.description == "description"
        assert product.stock == 10
        assert product.active
        assert product.created_at
        assert product.updated_at

    def test_update_product(self):
        product = Product(
            name="name",
            price=10.0,
            description="description",
            stock=10
        )

        product.update(
            name="new name",
            price=20.0,
            description="new description"
        )

        assert product.name == "new name"
        assert product.price == 20.0
        assert product.description == "new description"
        assert product.updated_at