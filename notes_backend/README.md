# Notes Backend (Flask)

A simple Flask backend providing CRUD operations for notes with in-memory storage using flask-smorest for OpenAPI documentation.

## Quick start

- Install dependencies:
  pip install -r requirements.txt

- Run the server:
  python run.py

- API Docs:
  - Swagger UI: /docs/
  - Redoc: /redoc

## Endpoints

- GET /             -> Health check
- GET /api/notes/   -> List notes
- POST /api/notes/  -> Create note
  Body: { "title": "str", "content": "str" }

- GET /api/notes/{id}    -> Get note by id
- PATCH /api/notes/{id}  -> Update note (partial)
  Body: { "title"?: "str", "content"?: "str" }

- DELETE /api/notes/{id} -> Delete note

## Environment

This project does not require environment variables, but a .env.example is included for future expansion.
