
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class GetProductInput:
    id: UUID

@dataclass
class GetProductOutput:
    id: UUID
    name: str
    price: float
    stock: int
    active: bool
    created_at: datetime
    updated_at: datetime

