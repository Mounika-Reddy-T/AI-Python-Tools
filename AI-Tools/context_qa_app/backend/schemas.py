from pydantic import BaseModel
from typing import Optional


class QueryRequest(BaseModel):
    context: str
    question: str


class LLMResponse(BaseModel):
    answer: str
    found: bool
    source_text: Optional[str]