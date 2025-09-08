"""
Routes for Notes CRUD operations.
"""

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ..services.note_service import note_service
from ..schemas.note import NoteSchema, NoteCreateSchema, NoteUpdateSchema

blp = Blueprint(
    "Notes",
    "notes",
    url_prefix="/api/notes",
    description="Operations for creating, reading, updating, and deleting notes",
)


@blp.route("/")
class NotesCollection(MethodView):
    """
    Collection endpoint for listing and creating notes.
    """

    @blp.response(200, NoteSchema(many=True))
    def get(self):
        """
        List all notes.
        Returns a list of note objects.
        """
        return [NoteSchema().dump(n) for n in note_service.list_notes()]

    @blp.arguments(NoteCreateSchema)
    @blp.response(201, NoteSchema)
    def post(self, json_data):
        """
        Create a new note.
        Body parameters:
        - title: string (required)
        - content: string (required)
        Returns the created note.
        """
        note = note_service.create_note(title=json_data["title"], content=json_data["content"])
        return NoteSchema().dump(note)


@blp.route("/<string:note_id>")
class NoteItem(MethodView):
    """
    Item endpoint for operations on a single note.
    """

    @blp.response(200, NoteSchema)
    def get(self, note_id: str):
        """
        Get a single note by ID.
        Path parameters:
        - note_id: string (required)
        """
        note = note_service.get_note(note_id)
        if not note:
            abort(404, message="Note not found")
        return NoteSchema().dump(note)

    @blp.arguments(NoteUpdateSchema)
    @blp.response(200, NoteSchema)
    def patch(self, json_data, note_id: str):
        """
        Update an existing note by ID. Partial updates supported.
        Path parameters:
        - note_id: string (required)
        Body parameters (any of):
        - title: string
        - content: string
        """
        note = note_service.update_note(
            note_id=note_id,
            title=json_data.get("title"),
            content=json_data.get("content"),
        )
        if not note:
            abort(404, message="Note not found")
        return NoteSchema().dump(note)

    @blp.response(204)
    def delete(self, note_id: str):
        """
        Delete a note by ID.
        Path parameters:
        - note_id: string (required)
        Returns no content upon success.
        """
        deleted = note_service.delete_note(note_id)
        if not deleted:
            abort(404, message="Note not found")
        return "", 204
