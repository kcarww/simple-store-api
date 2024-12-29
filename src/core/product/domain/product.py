from dataclasses import dataclass, field
from datetime import datetime
from core._shared.domain.entity import Entity

@dataclass(kw_only=True)
class Product(Entity):
    name: str
    price: float
    description: str
    stock: int
    active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


    def __post_init__(self):
        self.validade()

    def validade(self):
        self.validate_name()
        self.validate_price()

        if self.notification.has_errors:
            raise TypeError(self.notification.errors)

    def validate_name(self):
        if len(self.name) > 255:
            self.notification.add_error("Name cannot be longer than 255 characters")

        if not self.name:
            self.notification.add_error("Name cannot be empty")

    def validate_price(self):
        if self.price < 0:
            self.notification.add_error("Price cannot be negative")

    def validate_description(self):
        if len(self.description) > 255:
            self.notification.add_error("Description cannot be longer than 255 characters")


    def activate(self):
        self.active = True
        self.validade()

    def deactivate(self):
        self.active = False
        self.validade()

    def update(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description
        self.updated_at = datetime.now()
        self.validade()