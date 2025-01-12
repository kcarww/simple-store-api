from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

@dataclass(kw_only=True)
class UpdateProductInput:
    id: UUID
    name: str
    price: float
    description: str
    stock: int
    active: bool

@dataclass(kw_only=True)
class UpdateProductOutput:
    id: UUID
    name: str
    description: str
    price: float
    stock: int
    active: bool
    created_at: datetime
    updated_at: datetime = field(default_factory=datetime.now)