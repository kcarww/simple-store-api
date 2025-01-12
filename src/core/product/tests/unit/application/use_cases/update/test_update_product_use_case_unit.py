import pytest
from unittest.mock import Mock
from uuid import uuid4
from datetime import datetime
from src.core.product.application.use_cases.update.update_product_dto import (
    UpdateProductInput,
    UpdateProductOutput,
)
from src.core.product.application.use_cases.update.update_product_use_case import UpdateProductUseCase
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound


class TestUpdateProductUseCase:
    @pytest.fixture
    def mock_repository(self):
        return Mock()

    @pytest.fixture
    def use_case(self, mock_repository):
        return UpdateProductUseCase(product_repository=mock_repository)

    def test_execute_updates_product_successfully(self, use_case, mock_repository):
        product_id = uuid4()
        existing_product = Mock()
        existing_product.id = product_id
        existing_product.name = "Old Product"
        existing_product.price = 50.0
        existing_product.description = "Old description"
        existing_product.stock = 20
        existing_product.active = False
        existing_product.created_at = datetime(2023, 1, 1)
        existing_product.updated_at = datetime(2023, 1, 1)

        def update_mock(name, price, description, stock):
            existing_product.name = name
            existing_product.price = price
            existing_product.description = description
            existing_product.stock = stock

        existing_product.update.side_effect = update_mock
        mock_repository.find_by_id.return_value = existing_product

        input_data = UpdateProductInput(
            id=product_id,
            name="Updated Product",
            price=75.0,
            description="Updated description",
            stock=30,
            active=True,
        )

        result = use_case.execute(input_data)

        mock_repository.find_by_id.assert_called_once_with(product_id)
        existing_product.update.assert_called_once_with(
            input_data.name,
            input_data.price,
            input_data.description,
            input_data.stock,
        )
        mock_repository.update.assert_called_once_with(existing_product)
        assert result.name == "Updated Product"
        assert result.price == 75.0
        assert result.stock == 30
        assert result.description == "Updated description"

    def test_execute_raises_exception_when_product_not_found(self, use_case, mock_repository):
        product_id = uuid4()
        mock_repository.find_by_id.return_value = None

        input_data = UpdateProductInput(
            id=product_id,
            name="Non-existent Product",
            price=100.0,
            description="This product does not exist",
            stock=10,
            active=True,
        )

        with pytest.raises(ProductNotFound) as exc_info:
            use_case.execute(input_data)

       
        assert f"Product with id {product_id} not found" in str(exc_info.value)

        mock_repository.find_by_id.assert_called_once_with(product_id)

        mock_repository.update.assert_not_called()
    def test_execute_activates_product(self, use_case, mock_repository):
        product_id = uuid4()
        existing_product = Mock()
        existing_product.id = product_id
        existing_product.active = False

        mock_repository.find_by_id.return_value = existing_product

        input_data = UpdateProductInput(
            id=product_id,
            name="Product",
            price=50.0,
            description="Description",
            stock=10,
            active=True,
        )

        use_case.execute(input_data)

        existing_product.activate.assert_called_once()
        existing_product.deactivate.assert_not_called()

    def test_execute_deactivates_product(self, use_case, mock_repository):
        product_id = uuid4()
        existing_product = Mock()
        existing_product.id = product_id
        existing_product.active = True

        mock_repository.find_by_id.return_value = existing_product

        input_data = UpdateProductInput(
            id=product_id,
            name="Product",
            price=50.0,
            description="Description",
            stock=10,
            active=False,
        )

        use_case.execute(input_data)

        existing_product.deactivate.assert_called_once()
        existing_product.activate.assert_not_called()

    def test_execute_updates_timestamps_correctly(self, use_case, mock_repository):
        product_id = uuid4()
        existing_product = Mock()
        existing_product.id = product_id
        existing_product.updated_at = datetime(2023, 1, 1)

        def update_mock(name, price, description, stock):
            existing_product.updated_at = datetime.now()

        existing_product.update.side_effect = update_mock
        mock_repository.find_by_id.return_value = existing_product

        input_data = UpdateProductInput(
            id=product_id,
            name="Updated Product",
            price=75.0,
            description="Updated description",
            stock=30,
            active=True,
        )

        result = use_case.execute(input_data)

        assert result.updated_at > datetime(2023, 1, 1)
