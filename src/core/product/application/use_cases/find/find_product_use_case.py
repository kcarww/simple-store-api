from dataclasses import dataclass

from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.application.use_cases.find.find_product_dto import GetProductInput, GetProductOutput
from src.core.product.domain.product_repository import ProductRepositoryInterface

@dataclass(kw_only=True)
class FindProductUseCase:
    product_repository: ProductRepositoryInterface

    def execute(self, request: GetProductInput) -> GetProductOutput:
        product = self.product_repository.find(id=request.id)
        if product is None:
            raise ProductNotFound(f"Product with id {request.id} not found")

        return GetProductOutput(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            description=product.description,
            active=product.active,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )
