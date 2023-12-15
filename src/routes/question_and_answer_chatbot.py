from _testcapi import INT_MAX

from fastapi import APIRouter, Body
import os
from models.qna import QnA
from tflite_support.task import text
from utils.absolute_root import root_path

# Initialization of the ml model
answerer = text.BertQuestionAnswerer.create_from_file(root_path + '/public/ml_models/sample.tflite')

question_and_answer_chatbot_router = APIRouter()


@question_and_answer_chatbot_router.post("/", tags=["Question and Answer Chatbot"])
async def answer(input_values: QnA = Body(...)):
    bert_qa_result = answerer.answer(input_values.context, input_values.question)
    minimum = INT_MAX
    ans = {}
    for result in bert_qa_result.answers:
        if result.pos.logit < minimum:
            minimum = result.pos.logit
            ans = result.text
    return {
        "answer": ans
    }
