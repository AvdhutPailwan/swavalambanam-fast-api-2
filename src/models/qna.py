from pydantic import BaseModel


class QnA(BaseModel):
    context: str
    question: str
