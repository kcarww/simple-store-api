from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Notification:
    errors: list[str] = field(default_factory=list)

    def add_error(self, error: str) -> None:
        self.errors.append(error)

    @property
    def messages(self) -> str:
        return ','.join(self.errors)

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)
    
    def __str__(self) -> str:
        return self.messages