from _testcapi import INT_MAX

from fastapi import APIRouter, Request, Form, Body
import os

# Imports
from tflite_support.task import text

parent_dir_path = str(os.path.dirname(os.path.realpath(__file__)))
print(parent_dir_path.replace("/src/routes", ""))
parent_dir_path = parent_dir_path.replace("/src/routes", "")
# Initialization
answerer = text.BertQuestionAnswerer.create_from_file(parent_dir_path + '/public/ml_models/sample.tflite')

# Run inference
# bert_qa_result = answerer.answer(context, question)


question_and_answer_chatbot_router = APIRouter()


@question_and_answer_chatbot_router.post("/", tags=["Question and Answer Chatbot"])
async def answer(request: Request):
    input_values = dict(await request.json())
    bert_qa_result = answerer.answer(input_values['context'], input_values['question'])
    minimum = INT_MAX
    ans = {}
    for result in bert_qa_result.answers:
        if result.pos.logit < minimum:
            minimum = result.pos.logit
            ans = result.text
    return {
        "answer": ans
    }
