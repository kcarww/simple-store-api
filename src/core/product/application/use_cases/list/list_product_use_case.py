from dataclasses import dataclass

import config
from core.product.application.use_cases.list.list_product_dto import ListOutputMeta, ListProductOutput, ListProductRequest, ListProductResponse
from core.product.domain.product_repository import ProductRepositoryInterface

@dataclass
class ListProductUseCase:
    product_repository: ProductRepositoryInterface

    def execute(self, request: ListProductRequest) -> ListProductResponse:
        products = self.product_repository.find_all()
        sorted_products = sorted(
            [
                ListProductOutput(
                    id=product.id,
                    name=product.name,
                    price=product.price,
                    stock=product.stock,
                    active=product.active,
                    description=product.description,
                    created_at=product.created_at,
                    updated_at=product.updated_at,
                ) for product in products
            ], key=lambda product: getattr(product, request.order_by)
        )
        page_offset = (request.current_page - 1) * config.DEFAULT_PAGINATION_SIZE
        products_page = sorted_products[page_offset: page_offset + config.DEFAULT_PAGINATION_SIZE]

        return ListProductResponse(
            data=products_page,
            meta=ListOutputMeta(
                current_page=request.current_page,
                per_page=config.DEFAULT_PAGINATION_SIZE,
                total=len(sorted_products)
            )
        )
