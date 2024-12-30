from dataclasses import dataclass

from core.product.application.use_cases.create.create_product_dto import CreateProductInput, CreateProductOutput
from core.product.application.use_cases.exceptions.exceptions import InvalidProductData
from core.product.domain.product import Product
from core.product.domain.product_repository import ProductRepositoryInterface

@dataclass
class CreateProductUseCase:
    product_repository: ProductRepositoryInterface

    def execute(self, input: CreateProductInput) -> CreateProductOutput:
        try:
            product = Product(
                name=input.name,
                price=input.price,
                stock=input.stock,
                description=input.description,
            )
        except TypeError as error:
            raise InvalidProductData(error) from error
        
        self.product_repository.create(product)
        return CreateProductOutput(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            description=product.description,
            active=product.active,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )