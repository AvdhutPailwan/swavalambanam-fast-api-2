from fastapi import APIRouter, Body

from config.db import db
from schemas.quiz import quiz_entities

quiz = APIRouter()


@quiz.post("/", tags=["quiz"])
def get_chapter_quiz(chapter: str = Body(...)):
    question_objects = db.quiz.find({"Chapter": chapter})
    return {
        "questions": quiz_entities(question_objects)
    }
