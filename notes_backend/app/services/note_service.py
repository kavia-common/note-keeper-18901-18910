"""
Service layer implementing business logic and in-memory persistence for notes.
"""

from typing import Dict, List, Optional
from ..models.note import Note


class NoteService:
    """
    Provides CRUD operations for Note entities using in-memory storage.
    """

    def __init__(self) -> None:
        self._notes: Dict[str, Note] = {}

    # PUBLIC_INTERFACE
    def list_notes(self) -> List[Note]:
        """Return all notes."""
        return list(self._notes.values())

    # PUBLIC_INTERFACE
    def create_note(self, title: str, content: str) -> Note:
        """Create and store a new note."""
        note = Note.new(title=title, content=content)
        self._notes[note.id] = note
        return note

    # PUBLIC_INTERFACE
    def get_note(self, note_id: str) -> Optional[Note]:
        """Retrieve a note by ID or None if not found."""
        return self._notes.get(note_id)

    # PUBLIC_INTERFACE
    def update_note(self, note_id: str, title: Optional[str] = None, content: Optional[str] = None) -> Optional[Note]:
        """Update an existing note if it exists."""
        note = self._notes.get(note_id)
        if not note:
            return None
        note.update_with(title=title, content=content)
        return note

    # PUBLIC_INTERFACE
    def delete_note(self, note_id: str) -> bool:
        """Delete a note by ID. Returns True if deleted."""
        return self._notes.pop(note_id, None) is not None


# Module-level singleton for simple usage throughout the app lifecycle
note_service = NoteService()
