from uuid import UUID
from dataclasses import dataclass

from core.product.domain.product import Product
from core.product.domain.product_repository import ProductRepositoryInterface
from django_project.product.models import Product as ProductModel


@dataclass(kw_only=True)
class DjangoORMProductRepository(ProductRepositoryInterface):
    product_model: ProductModel = ProductModel

    def create(self, product: Product) -> None:
        product_orm = ProductModelMapper.to_model(product)
        product_orm.save()

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def find(self, id):
        pass

    def find_all(self) -> list[Product]:
        return [
            ProductModelMapper.to_entity(product)
            for product in self.product_model.objects.all()
        ]

@dataclass
class ProductModelMapper:
    @staticmethod
    def to_entity(product: ProductModel) -> Product:
        return Product(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            description=product.description,
            created_at=product.created_at,
            updated_at=product.updated_at
        )
    
    @staticmethod
    def to_model(product: Product) -> ProductModel:
        return ProductModel(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            description=product.description,
            created_at=product.created_at,
            updated_at=product.updated_at
        )