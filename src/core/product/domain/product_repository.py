from dataclasses import dataclass

from src.core._shared.domain.repository_interface import RepositoryInterface

@dataclass(kw_only=True)
class ProductRepositoryInterface(RepositoryInterface):
    ...