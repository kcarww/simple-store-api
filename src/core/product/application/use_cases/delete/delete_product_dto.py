from dataclasses import dataclass
from uuid import UUID

@dataclass(kw_only=True)
class DeleteProductInput:
    id: UUID