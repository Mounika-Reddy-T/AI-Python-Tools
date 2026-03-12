from fastapi import FastAPI, HTTPException
from models import QuestionRequest, EvaluationResult
from evaluator import generate_answer, judge_answer

app = FastAPI(
    title="AI Prompt Evaluation Tool",
    description="Evaluate AI responses to questions",
    version="1.0.0"
)


@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "running", "message": "AI Prompt Evaluation Tool"}


@app.post("/evaluate", response_model=EvaluationResult)
def evaluate_question(request: QuestionRequest):
    """
    Evaluate a single question:
    1. Generate answer using generator model
    2. Evaluate answer quality using judge model
    3. Return results with score
    """
    try:
        # Generate answer
        answer = generate_answer(request.question)
        
        # Evaluate answer
        evaluation = judge_answer(request.question, answer)
        
        # Calculate score (1 for correct, 0 for incorrect)
        score = 1 if "correct" in evaluation.lower() else 0
        
        return EvaluationResult(
            question=request.question,
            answer=answer,
            evaluation=evaluation,
            score=score
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")