from uuid import uuid4

import pytest
from src.core.product.application.use_cases.delete.delete_product_dto import DeleteProductInput
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.application.use_cases.delete.delete_product_use_case import DeleteProductUseCase
from src.core.product.domain.product import Product
from src.core.product.infra.in_memory.in_memory_product_repository import InMemoryProductRepository


class TestDeleteProductUseCase:
    def test_delete_existent_product(self):
        product = Product(
            name="Product 1",
            description="Description of Product 1",
            price=100.0,
            stock=10,
        )
        repository = InMemoryProductRepository(items=[product])
        use_case = DeleteProductUseCase(product_repository=repository)
        response = use_case.execute(DeleteProductInput(id=product.id))
        assert response is None

    def test_delete_non_existent_product(self):
        repository = InMemoryProductRepository(items=[])
        use_case = DeleteProductUseCase(product_repository=repository)
        non_existent_product_id = uuid4()
        with pytest.raises(ProductNotFound) as exce_info:
            use_case.execute(DeleteProductInput(id=non_existent_product_id))

        