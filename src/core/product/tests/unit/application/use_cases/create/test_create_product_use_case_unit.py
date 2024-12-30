import pytest
from unittest.mock import Mock
from datetime import datetime

from core.product.application.use_cases.create.create_product_dto import CreateProductInput
from core.product.application.use_cases.create.create_product_use_case import CreateProductUseCase
from core.product.application.use_cases.exceptions.exceptions import InvalidProductData


class TestCreateProductUseCase:
    @pytest.fixture
    def mock_repository(self):
        return Mock()

    @pytest.fixture
    def use_case(self, mock_repository):
        return CreateProductUseCase(product_repository=mock_repository)

    def test_execute_creates_product_successfully(self, use_case, mock_repository):
        input_data = CreateProductInput(
            name="Test Product",
            price=100.0,
            stock=50,
            description="A test product",
            active=False
        )
        mock_repository.create.return_value = None  


        result = use_case.execute(input_data)


        mock_repository.create.assert_called_once()  
        product_created = mock_repository.create.call_args[0][0]  
        assert product_created.name == input_data.name
        assert product_created.price == input_data.price
        assert product_created.stock == input_data.stock
        assert product_created.description == input_data.description

        assert result.name == input_data.name
        assert result.price == input_data.price
        assert result.stock == input_data.stock
        assert isinstance(result.created_at, datetime)
        assert isinstance(result.updated_at, datetime)

    def test_execute_raises_exception_with_invalid_data(self, use_case, mock_repository):

        input_data = CreateProductInput(
            name="",  
            price=-100.0,  
            stock=50,
            description="A test product",
            active=True
        )


        with pytest.raises(InvalidProductData) as exc_info:
            use_case.execute(input_data)

        
        assert "Name cannot be empty" in str(exc_info.value)
        mock_repository.create.assert_not_called()  