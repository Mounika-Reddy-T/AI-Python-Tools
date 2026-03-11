from typing import Optional

from pydantic import BaseModel


class QueryRequest(BaseModel):
    context: str
    question: str


class LLMResponse(BaseModel):
    answer: str
    found: bool
    source_text: Optional[str]