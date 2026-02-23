from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

@dataclass
class Query:
    """Domain entity represents user query"""

    id: UUID
    text: str
    conversetion_id: UUID | None = None
    created_at: datetime = field(default_factory=datetime.now(tz="UTC"))

    def __post_init__(self) -> None:
        if not self.text:
            raise ValueError("Query Text cannot be empty")
        
    