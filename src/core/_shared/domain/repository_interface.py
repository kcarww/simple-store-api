from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic


T = TypeVar('T')

@dataclass(kw_only=True)
class RepositoryInterface(Generic[T], ABC):
    @abstractmethod
    def create(self, entity: T) -> None:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def find(self, id: int) -> T:
        pass

    @abstractmethod
    def find_all(self) -> list[T]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
