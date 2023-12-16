import google.generativeai as genai
import joblib
from fastapi import APIRouter, Body
from starlette.responses import JSONResponse

from models.interest_based_learning import Example, Suggestion
from utils.absolute_root import root_path
from config.db import db
from schemas.interest_based_learning import theory_entity, theories_entity

interest_based_learning_router = APIRouter()

# interest based model
learning_style_predictor = joblib.load(root_path + '/public/ml_models/learning_style_classifier1.pkl')

# Generative model

genai.configure(api_key="AIzaSyD_E97C3XZ4I0XLV4vY-xndsfqgac3TcKA")
# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


# prompt_parts = [
#     "give example of law of inertia in context of cricket",
# ]
#
# response = model.generate_content(prompt_parts)
# print(response.text)


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
def give_example(example: Example = Body(...)):
    prompt_parts = [
        f"give example of {example.topic} from {example.subject} in context of {example.interest}",
        "in layman terms",
        "without markdown syntax"
    ]

    response = model.generate_content(prompt_parts)
    # print(response.text)
    return {
        "answer": response.text
    }


@interest_based_learning_router.post('/show_theory', tags=["Interest Based Learning"])
async def theory_of_chapter(chapter_name = Body(...)):
    data = db.chapters.find_one({"chapter_name": chapter_name})
    chapter_content = theory_entity(data)
    return chapter_content