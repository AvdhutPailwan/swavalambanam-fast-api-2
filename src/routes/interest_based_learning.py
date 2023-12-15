import joblib
from fastapi import APIRouter, Request

interest_based_learning_router = APIRouter()

# loaded_model = joblib.load('ScaledLogReg.pkl')
# prediction=loaded_model.predict([[70, 20]])



@interest_based_learning_router.get("/", tags=["Interest Based Learning"])
def welcome_route():
    return {
        "message": "Welcome to Interest Based Learning Route"
    }


@interest_based_learning_router.post("/", tags=["Interest Based Learning"], )
async def test_post(request: Request):
    arg = dict(await request.json())
    print(arg["test_score"], " ", arg["average_quiz_time"])
    return True
