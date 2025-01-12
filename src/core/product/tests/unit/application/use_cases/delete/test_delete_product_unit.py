from unittest.mock import Mock
from uuid import uuid4
import pytest

from src.core.product.application.use_cases.delete.delete_product_dto import DeleteProductInput
from src.core.product.application.use_cases.delete.delete_product_use_case import DeleteProductUseCase
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.domain.product import Product

class TestDeleteProductUnit:
    @pytest.fixture
    def mock_repository(self):
        return Mock()
    
    @pytest.fixture
    def use_case(self, mock_repository):
        return DeleteProductUseCase(product_repository=mock_repository)
    
    def test_execute_deletes_product(self, use_case, mock_repository):
        produto = Product(
            name="Product A",
            price=10,
            stock=10,
            active=True,
            description="Product A description"
        )
        mock_repository.find.return_value = produto

        use_case.execute(DeleteProductInput(
            id=produto.id
        ))

        mock_repository.delete.assert_called_once_with(produto.id)

    def test_when_product_does_not_exists_then_raises_error(self, use_case, mock_repository):
        mock_repository.find.return_value = None
        invalid_id = uuid4()
        with pytest.raises(ProductNotFound) as exc:
            use_case.execute(DeleteProductInput(
                id=invalid_id
            ))

        assert str(exc.value) == f"Product with id {invalid_id} not found"