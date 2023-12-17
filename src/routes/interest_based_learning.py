import joblib
from dotenv import load_dotenv
from fastapi import APIRouter, Body

from config.db import db
from models.interest_based_learning import Example, Suggestion
from schemas.interest_based_learning import theory_entity
from utils.absolute_root import root_path
from utils.generative_model import model

load_dotenv()
interest_based_learning_router = APIRouter()

# interest based model
learning_style_predictor = joblib.load(root_path + '/public/ml_models/learning_style_classifier1.pkl')


# ----------------------------------------------------------------------------------
@interest_based_learning_router.get("/", tags=["Interest Based Learning"])
def welcome_route():
    return f'welcome to the interest based learning route'


@interest_based_learning_router.post("/learning_style_suggestion", tags=["Interest Based Learning"], )
def suitable_learning_style(data: Suggestion):
    learning_style = learning_style_predictor.predict([[int(data.avg_time), int(data.quiz_score)]])
    print(learning_style[0])
    return {
        "learning_recommended": learning_style[0]
    }


@interest_based_learning_router.post("/give_example", tags=["Interest Based Learning"])
async def give_example(example: Example = Body(...)):
    prompt_parts = [
        f"give example of {example.topic} from {example.subject} in context of {example.interest}",
        "in layman terms",
        "without markdown syntax"
    ]

    response = model.generate_content(prompt_parts)
    return {
        "answer": response.text
    }


@interest_based_learning_router.post('/show_theory', tags=["Interest Based Learning"])
async def theory_of_chapter(chapter_name=Body(...)):
    data = db.chapters.find_one({"chapter_name": chapter_name})
    chapter_content = theory_entity(data)
    return chapter_content
