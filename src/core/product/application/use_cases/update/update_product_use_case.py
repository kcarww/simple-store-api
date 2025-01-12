from dataclasses import dataclass

from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.application.use_cases.update.update_product_dto import UpdateProductInput, UpdateProductOutput
from src.core.product.domain.product_repository import ProductRepositoryInterface

@dataclass(kw_only=True)
class UpdateProductUseCase:
    product_repository: ProductRepositoryInterface

    def execute(self, request: UpdateProductInput) -> UpdateProductOutput:
        product = self.product_repository.find(request.id)

        if product is None:
            raise ProductNotFound(f"Product with id {request.id} not found")

        
        if request.active:
            product.activate()

        if not request.active:
            product.deactivate()
            

        product.update(request.name, request.price, request.description, request.stock)

        self.product_repository.update(product)
        
        return UpdateProductOutput(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            description=product.description,
            active=product.active,
            created_at=product.created_at,
            updated_at=product.updated_at,
       )