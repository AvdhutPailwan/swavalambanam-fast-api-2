from fastapi import APIRouter, Request
from models.note import Note
from config.db import connection
from schemas.note import note_entity, notes_entity

note = APIRouter()


@note.get("/")
def note_router(request: Request):
    return f"This is note router"
