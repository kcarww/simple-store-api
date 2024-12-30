from src.core.product.application.use_cases.list.list_product_use_case import (
    ListProductUseCase,
    ListProductRequest,
)
from src.core.product.application.use_cases.create.create_product_dto import CreateProductInput
from src.core.product.infra.in_memory.in_memory_product_repository import InMemoryProductRepository
from src.core.product.domain.product import Product


class TestListProductUseCaseIntegration:
    def test_list_product_use_case(self):
        repository = InMemoryProductRepository()

        products = [
            Product(
                id=None,
                name="Product A",
                description="Description for Product A",
                price=50.0,
                stock=15,
                active=True,
                created_at=None,
                updated_at=None,
            ),
            Product(
                id=None,
                name="Product B",
                description="Description for Product B",
                price=100.0,
                stock=10,
                active=True,
                created_at=None,
                updated_at=None,
            ),
        ]
        for product in products:
            repository.create(product)

        request = ListProductRequest(order_by="name", current_page=1)
        use_case = ListProductUseCase(repository)

        response = use_case.execute(request)

        assert response.meta.current_page == 1
        assert response.meta.total == len(products)
        assert len(response.data) == len(products)
        assert response.data[0].name == "Product A" 
        assert response.data[1].name == "Product B"
