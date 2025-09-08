"""
Note model definitions.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class Note:
    """
    Represents a Note entity in memory.
    """
    id: str
    title: str
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @staticmethod
    # PUBLIC_INTERFACE
    def new(title: str, content: str) -> "Note":
        """Create a new Note with a generated ID and timestamps."""
        now = datetime.utcnow()
        return Note(id=str(uuid.uuid4()), title=title, content=content, created_at=now, updated_at=now)

    # PUBLIC_INTERFACE
    def update_with(self, title: Optional[str] = None, content: Optional[str] = None) -> None:
        """Update the note fields and refresh updated_at."""
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        self.updated_at = datetime.utcnow()
