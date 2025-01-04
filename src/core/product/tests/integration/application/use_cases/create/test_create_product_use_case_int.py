from src.core.product.application.use_cases.create.create_product_dto import CreateProductInput
from src.core.product.application.use_cases.create.create_product_use_case import CreateProductUseCase
from src.core.product.infra.in_memory.in_memory_product_repository import InMemoryProductRepository


class TestCreateProductUseCaseIntegration:
    def test_create_product_use_case(self):
        repository = InMemoryProductRepository()
        input = CreateProductInput(
            name="Product 1",
            description="Description of Product 1",
            price=100.0,
            stock=10,
            active=True
        )
        use_case = CreateProductUseCase(repository)
        output = use_case.execute(input)

        assert output.id is not None
        assert output.name == input.name
        assert output.description == input.description
        assert output.price == input.price
        assert output.stock == input.stock
        assert output.created_at is not None
        assert output.updated_at is not None
