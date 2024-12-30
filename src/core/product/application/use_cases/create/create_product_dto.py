from dataclasses import dataclass
import datetime
from typing import Optional

@dataclass(kw_only=True)
class CreateProductInput:
    name: str
    description: Optional[str]
    price: float
    stock: int

@dataclass(kw_only=True)
class CreateProductOutput:
    id: str
    name: str
    description: Optional[str]
    price: float
    stock: int
    active: bool
    created_at: datetime
    updated_at: datetime

