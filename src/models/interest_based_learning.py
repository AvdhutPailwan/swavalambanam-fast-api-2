from pydantic import BaseModel


class Suggestion(BaseModel):
    content_type: str
    quiz_score: int
    avg_time: int
    interest: str

class Example(BaseModel):
    topic: str
    subject: str
    interest: str