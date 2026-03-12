from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class EvaluationResult(BaseModel):
    question: str
    answer: str
    evaluation: str
    score: int