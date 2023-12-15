import os

import joblib
from fastapi import APIRouter, Request, Query
import google.generativeai as genai

interest_based_learning_router = APIRouter()

# loaded_model = joblib.load('ScaledLogReg.pkl')
# prediction=loaded_model.predict([[70, 20]])

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


@interest_based_learning_router.post("/", tags=["Interest Based Learning"], )
async def test_post(request: Request):
    arg = dict(await request.json())
    print(arg["test_score"], " ", arg["average_quiz_time"])
    return True

@interest_based_learning_router.get("/give_expample/{topic:str, interest:str, subject:str}", tags=["Interest Based Learning"])
def give_example(topic:str = Query(...), interest:str = Query(...), subject:str = Query(...)):
    prompt_parts = [
        f"give example of {topic} from {subject} in context of {interest}",
        "in layman terms",
        "without markdown syntax"
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)
    return response.text