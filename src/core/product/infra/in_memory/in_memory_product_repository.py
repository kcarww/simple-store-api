from dataclasses import dataclass, field

from core.product.domain.product import Product
from core.product.domain.product_repository import ProductRepositoryInterface

@dataclass(kw_only=True)
class InMemoryProductRepository(ProductRepositoryInterface):
    items: list = field(default_factory=list)

    def create(self, product: Product) -> None:
        self.items.append(product)

    def find(self, id: str) -> Product:
        for product in self.items:
            if product.id == id:
                return product
        return None

    def find_all(self) -> list[Product]:
        return [product for product in self.items]
    
    def update(self, product: Product) -> None:
        for i, p in enumerate(self.items):
            if p.id == product.id:
                self.items[i] = product
                return
            
    def delete(self, id: str) -> None:
        for i, product in enumerate(self.items):
            if product.id == id:
                del self.items[i]
                return
    
