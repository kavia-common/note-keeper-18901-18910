"""
Marshmallow schemas for Notes.
"""

from marshmallow import Schema, fields, validate


class NoteBaseSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1), metadata={"description": "Title of the note"})
    content = fields.Str(required=True, metadata={"description": "Body content of the note"})


class NoteCreateSchema(NoteBaseSchema):
    """
    Schema for creating a note.
    """
    pass


class NoteUpdateSchema(Schema):
    """
    Schema for updating a note (partial).
    """
    title = fields.Str(required=False, validate=validate.Length(min=1), metadata={"description": "Title of the note"})
    content = fields.Str(required=False, metadata={"description": "Body content of the note"})


class NoteSchema(NoteBaseSchema):
    """
    Full Note schema for responses.
    """
    id = fields.Str(required=True, metadata={"description": "Unique identifier of the note"})
    created_at = fields.DateTime(required=True, metadata={"description": "Creation timestamp (UTC)"})
    updated_at = fields.DateTime(required=True, metadata={"description": "Last update timestamp (UTC)"})
