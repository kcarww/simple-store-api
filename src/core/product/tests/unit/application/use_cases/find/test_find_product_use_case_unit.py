import pytest
from unittest.mock import Mock
from datetime import datetime
from uuid import uuid4

from src.core.product.application.use_cases.find.find_product_dto import GetProductInput, GetProductOutput
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.application.use_cases.find.find_product_use_case import FindProductUseCase
from src.core.product.domain.product import Product


class TestFindProductUseCase:
    @pytest.fixture
    def mock_repository(self):
        return Mock()

    @pytest.fixture
    def use_case(self, mock_repository):
        return FindProductUseCase(product_repository=mock_repository)

    def test_execute_returns_product(self, use_case, mock_repository):
        product_id = str(uuid4())
        mock_product = Product(
            id=product_id,
            name="Product A",
            price=100.0,
            stock=10,
            active=True,
            description="Product A description",
            created_at=datetime(2024, 1, 1, 12, 0, 0),
            updated_at=datetime(2024, 1, 1, 12, 0, 0),
        )
        mock_repository.find.return_value = mock_product
        request = GetProductInput(id=product_id)

        response = use_case.execute(request)

        mock_repository.find.assert_called_once_with(product_id)
        assert isinstance(response, GetProductOutput)
        assert response.id == product_id
        assert response.name == "Product A"
        assert response.price == 100.0
        assert response.stock == 10
        assert response.active is True
        assert response.created_at == datetime(2024, 1, 1, 12, 0, 0)
        assert response.updated_at == datetime(2024, 1, 1, 12, 0, 0)

    def test_execute_raises_product_not_found(self, use_case, mock_repository):
        product_id = str(uuid4())
        mock_repository.find.return_value = None
        request = GetProductInput(id=product_id)

        with pytest.raises(ProductNotFound) as exc_info:
            use_case.execute(request)

        mock_repository.find.assert_called_once_with(product_id)
        assert str(exc_info.value) == f"Product with id {product_id} not found"
