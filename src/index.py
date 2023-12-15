# uvicorn index:app --reload

from dotenv import load_dotenv
from fastapi import FastAPI
from routes.note import note
from routes.interest_based_learning import interest_based_learning_router

load_dotenv()

app = FastAPI()

app.include_router(note, prefix="/notes")
app.include_router(interest_based_learning_router, prefix="/interest_based_learning")
