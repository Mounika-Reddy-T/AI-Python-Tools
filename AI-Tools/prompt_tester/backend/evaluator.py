from config import GENERATOR_MODEL, JUDGE_MODEL
from openrouter_client import call_model
from prompts import ANSWER_GENERATION_PROMPT, EVALUATION_SYSTEM_PROMPT, EVALUATION_USER_PROMPT


def generate_answer(question):
    """Generate answer using the generator model."""
    messages = [
        {"role": "system", "content": ANSWER_GENERATION_PROMPT},
        {"role": "user", "content": question}
    ]
    return call_model(GENERATOR_MODEL, messages)


def judge_answer(question, answer):
    """Evaluate answer quality using the judge model."""
    messages = [
        {"role": "system", "content": EVALUATION_SYSTEM_PROMPT},
        {"role": "user", "content": EVALUATION_USER_PROMPT.format(question=question, answer=answer)}
    ]
    return call_model(JUDGE_MODEL, messages)