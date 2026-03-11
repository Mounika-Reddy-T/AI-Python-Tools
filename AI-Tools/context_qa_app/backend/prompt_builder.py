SYSTEM_PROMPT = """
You are a context-restricted AI assistant.

Rules:
1. Answer ONLY from the provided context.
2. Do NOT use outside knowledge.
3. If the answer is not in the context return "Not in context".
4. Output MUST be valid JSON.
5. Do not output anything outside JSON.

JSON format:

{
 "answer": "string",
 "found": boolean,
 "source_text": "string or null"
}
"""


def build_prompt(context: str, question: str) -> str:
    """Build user prompt with context and question."""

    return f"""
Context:
{context}

Question:
{question}

Answer strictly from the context.
If the answer does not exist return "Not in context".

Return JSON only.
"""