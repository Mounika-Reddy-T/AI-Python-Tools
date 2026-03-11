from fastapi import FastAPI, HTTPException
from schemas import QueryRequest, LLMResponse
from prompt_builder import SYSTEM_PROMPT, build_prompt
from llm_service import ask_llm
import json

app = FastAPI()


def validate_json(text):

    try:
        data = json.loads(text)

        if not all(k in data for k in ["answer", "found", "source_text"]):
            raise ValueError()

        return data

    except Exception:

        return {
            "answer": "Not in context",
            "found": False,
            "source_text": None
        }


@app.post("/ask", response_model=LLMResponse)
async def ask_question(payload: QueryRequest):

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
