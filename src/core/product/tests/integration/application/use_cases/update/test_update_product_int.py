from uuid import uuid4
from src.core.product.application.use_cases.update.update_product_dto import UpdateProductInput
from src.core.product.application.use_cases.update.update_product_use_case import UpdateProductUseCase
from src.core.product.application.use_cases.create.create_product_dto import CreateProductInput
from src.core.product.application.use_cases.create.create_product_use_case import CreateProductUseCase
from src.core.product.infra.in_memory.in_memory_product_repository import InMemoryProductRepository
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound

class TestUpdateProductUseCaseIntegration:
    def test_update_existing_product(self):
        repository = InMemoryProductRepository()
        create_use_case = CreateProductUseCase(repository)

        create_input = CreateProductInput(
            name="Product 1",
            description="Description of Product 1",
            price=100.0,
            stock=10,
            active=True
        )
        created_product = create_use_case.execute(create_input)

        update_use_case = UpdateProductUseCase(product_repository=repository)
        update_input = UpdateProductInput(
            id=created_product.id,
            name="Updated Product 1",
            description="Updated Description of Product 1",
            price=200.0,
            stock=15,
            active=False
        )

        updated_product = update_use_case.execute(update_input)

        assert updated_product.id == created_product.id
        assert updated_product.name == update_input.name
        assert updated_product.description == update_input.description
        assert updated_product.price == update_input.price
        assert updated_product.stock == update_input.stock
        assert updated_product.active == update_input.active
        assert updated_product.created_at == created_product.created_at
        assert updated_product.updated_at > created_product.updated_at

    def test_update_nonexist_product(self):
        repository = InMemoryProductRepository()
        update_use_case = UpdateProductUseCase(product_repository=repository)

        update_input = UpdateProductInput(
            id=uuid4(),
            name="Nonexistent Product",
            description="Nonexistent Description",
            price=150.0,
            stock=20,
            active=True
        )

        try:
            update_use_case.execute(update_input)
        except ProductNotFound as e:
            assert str(e) == f"Product with id {update_input.id} not found"
        else:
            assert False, "Expected ProductNotFound exception was not raised"
