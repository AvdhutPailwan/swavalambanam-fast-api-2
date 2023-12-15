from pydantic import BaseModel


class Example(BaseModel):
    topic: str
    subject: str
    interest: str