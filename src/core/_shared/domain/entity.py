from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from src.core._shared.domain.notification import Notification

@dataclass(kw_only=True)
class Entity(ABC):
    id: UUID = field(default_factory=uuid4)
    notification: Notification = field(default_factory=Notification)

    def __eq__(self, other: "Entity") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return other.id == self.id
    
    @abstractmethod
    def validade(self):
        pass