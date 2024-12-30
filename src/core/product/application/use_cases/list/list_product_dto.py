from abc import ABC
from ast import TypeVar
from dataclasses import dataclass, field
from typing import Generic, TypeVar
from uuid import UUID

import config


@dataclass
class ListProductRequest:
    order_by: str = "name"
    current_page: int = 1


@dataclass
class ListProductOutput:
    id: UUID
    name: str
    price: float
    stock: int
    active: bool
    description: str
    created_at: str
    updated_at: str

@dataclass
class ListOutputMeta:
    current_page: int = 1
    per_page: int = config.DEFAULT_PAGINATION_SIZE
    total: int = 0

T = TypeVar("T")

@dataclass
class ListProductResponse(Generic[T], ABC):
    data: list[T]
    meta: ListOutputMeta = field(default_factory=ListOutputMeta)


