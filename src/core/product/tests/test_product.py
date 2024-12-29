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