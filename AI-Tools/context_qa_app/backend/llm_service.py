import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


async def ask_llm(system_prompt: str, user_prompt: str) -> str:
    """Send prompts to LLM and return response."""
    if not OPENROUTER_API_KEY:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not configured. Add it to your environment or .env file."
        )

    payload = {
        "model": "openai/gpt-4o-mini",
        "temperature": 0,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "context-qa-app",
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload
        )

    try:
        data = response.json()
    except json.JSONDecodeError as exc:
        print(f"OpenRouter response status: {response.status_code}")
        print(f"OpenRouter response text: {response.text}")
        raise RuntimeError(
            f"OpenRouter returned a non-JSON response (status {response.status_code})."
        ) from exc

    if response.status_code >= 400:
        error_message = data.get("error", {}).get("message", "Unknown OpenRouter error")
        print(f"OpenRouter error response: {data}")
        raise RuntimeError(f"OpenRouter error ({response.status_code}): {error_message}")

    choices = data.get("choices")
    if not choices:
        raise RuntimeError("Invalid response from OpenRouter: missing choices")

    message = choices[0].get("message", {})
    content = message.get("content")
    if not content:
        raise RuntimeError("Invalid response from OpenRouter: missing message content")

    return content
