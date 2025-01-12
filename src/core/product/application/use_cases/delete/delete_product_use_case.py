from dataclasses import dataclass

from src.core.product.application.use_cases.delete.delete_product_dto import DeleteProductInput
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.domain.product_repository import ProductRepositoryInterface

@dataclass(kw_only=True)
class DeleteProductUseCase:
    product_repository: ProductRepositoryInterface


    def execute(self, request: DeleteProductInput) -> None:
        product = self.product_repository.find(request.id)
        if product is None:
            raise ProductNotFound(f"Product with id {request.id} not found")
        
        self.product_repository.delete(request.id)