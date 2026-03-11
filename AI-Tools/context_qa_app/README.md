# Context QA App

A small FastAPI service that answers a question strictly from user-provided context using OpenRouter.

## What It Does

- Accepts a `context` string and a `question`
- Sends both to an LLM with a strict JSON-only prompt
- Returns:
  - `answer`
  - `found`
  - `source_text`

If the answer is not present in the provided context, the service returns `"Not in context"`.

## Project Structure

```text
context_qa_app/
  backend/
    main.py
    llm_service.py
    prompt_builder.py
    schemas.py
  frontend/
    index.html
```

Note: `frontend/index.html` is currently empty, so the working part of this project is the backend API.

## Requirements

- Python 3.10+
- An `OPENROUTER_API_KEY`

## Environment Variables

Create or update your root `.env` file with:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

## Install Dependencies

If you do not already have the required packages installed:

```powershell
pip install fastapi uvicorn httpx python-dotenv pydantic
```

## Run The API

From the backend folder:

```powershell
cd C:\Users\Ahex-Tech\Desktop\AI\context_qa_app\backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

If port `8000` is already in use, run on a different port:

```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8001
```

## API Endpoint

### `POST /ask`

Request body:

```json
{
  "context": "Alice joined the company in 2022 and works in product.",
  "question": "When did Alice join the company?"
}
```

Successful response:

```json
{
  "answer": "Alice joined the company in 2022.",
  "found": true,
  "source_text": "Alice joined the company in 2022 and works in product."
}
```

Fallback response when the answer is not in the context:

```json
{
  "answer": "Not in context",
  "found": false,
  "source_text": null
}
```

## Notes

- The model is configured in [llm_service.py](C:\Users\Ahex-Tech\Desktop\AI\context_qa_app\backend\llm_service.py).
- The prompt contract is defined in [prompt_builder.py](C:\Users\Ahex-Tech\Desktop\AI\context_qa_app\backend\prompt_builder.py).
- Upstream OpenRouter failures are returned as HTTP `502`.

