import json

from fastapi import FastAPI, HTTPException

from llm_service import ask_llm
from prompt_builder import SYSTEM_PROMPT, build_prompt
from schemas import LLMResponse, QueryRequest

app = FastAPI()


def validate_json(text: str) -> dict:
    """Validate and parse JSON response from LLM."""
    try:
        data = json.loads(text)
        if not all(k in data for k in ["answer", "found", "source_text"]):
            raise ValueError("Missing required fields")
        return data
    except (json.JSONDecodeError, ValueError):
        return {
            "answer": "Not in context",
            "found": False,
            "source_text": None
        }


@app.post("/ask", response_model=LLMResponse)
async def ask_question(payload: QueryRequest) -> dict:
    """Process question with context and return LLM response."""

    if not payload.context.strip():
        return {
            "answer": "Not in context",
            "found": False,
            "source_text": None
        }

    prompt = build_prompt(payload.context, payload.question)

    try:
        llm_output = await ask_llm(SYSTEM_PROMPT, prompt)
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    result = validate_json(llm_output)

    return result
