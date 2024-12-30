from core.product.domain.product import Product
from core.product.infra.in_memory.in_memory_product_repository import InMemoryProductRepository


class TestInMemoryProductRepository:
    def test_can_save_product(self):
        repository = InMemoryProductRepository()
        product = Product(
            name="Product 1",
            description="Description 1",
            price=10.0,
            stock=10,
        )
        repository.create(product)
        assert repository.find(product.id) == product
        assert len(repository.items) == 1

    def test_can_update_product(self):
        repository = InMemoryProductRepository()
        product = Product(
            name="Product 1",
            description="Description 1",
            price=10.0,
            stock=10,
        )
        repository.create(product)
        product.name = "Product 2"
        repository.update(product)
        assert repository.find(product.id) == product
        assert len(repository.items) == 1

    def test_can_delete_product(self):
        repository = InMemoryProductRepository()
        product = Product(
            name="Product 1",
            description="Description 1",
            price=10.0,
            stock=10,
        )
        repository.create(product)
        repository.delete(product.id)
        assert repository.find(product.id) is None
        assert len(repository.items) == 0

    def test_can_list_products(self):
        repository = InMemoryProductRepository()
        product1 = Product(
            name="Product 1",
            description="Description 1",
            price=10.0,
            stock=10,
        )
        product2 = Product(
            name="Product 2",
            description="Description 2",
            price=20.0,
            stock=20,
        )
        repository.create(product1)
        repository.create(product2)
        assert repository.find_all() == [product1, product2]
        assert len(repository.items) == 2
