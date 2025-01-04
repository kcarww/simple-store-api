from src.core.product.application.use_cases.find.find_product_use_case import (
    FindProductUseCase,
)
from src.core.product.application.use_cases.find.find_product_dto import (
    GetProductInput,
)
from src.core.product.infra.in_memory.in_memory_product_repository import (
    InMemoryProductRepository,
)
from src.core.product.domain.product import Product
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound


class TestFindProductUseCaseIntegration:
    def test_find_product_use_case(self):
        repository = InMemoryProductRepository()

        product = Product(
            name="Product A",
            description="Description for Product A",
            price=50.0,
            stock=15,
            active=True,
            created_at=None,
            updated_at=None,
        )
        repository.create(product)

        request = GetProductInput(id=product.id)
        use_case = FindProductUseCase(product_repository=repository)

        response = use_case.execute(request)

        assert response.id == product.id
        assert response.name == product.name
        assert response.price == product.price
        assert response.stock == product.stock
        assert response.active == product.active

    def test_find_product_raises_not_found(self):
        repository = InMemoryProductRepository()

        request = GetProductInput(id="non-existent-id")
        use_case = FindProductUseCase(product_repository=repository)

        try:
            use_case.execute(request)
            assert False, "Expected ProductNotFound exception"
        except ProductNotFound as e:
            assert str(e) in "Product with id non-existent-id not found"
