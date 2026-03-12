# AI Prompt Evaluation Tool

A clean, efficient tool to test AI responses and get automatic evaluation scores.

## Features

- 🤖 **AI Answer Generation**: Uses OpenAI GPT-5-nano
- 🔍 **Automatic Evaluation**: Uses OpenAI GPT-4.1-nano for scoring
- 📊 **CSV Export**: Automatic saving with timestamps
- 🎯 **Simple Interface**: Clean Streamlit UI

## Quick Start

1. **Install dependencies:**
```bash
pip install fastapi uvicorn streamlit pandas requests python-dotenv
```

2. **Start backend:**
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

3. **Start frontend:**
```bash
python -m streamlit run frontend/app.py
```

4. **Open browser:** http://localhost:8501

## Project Structure

```
prompt_tester/
├── backend/
│   ├── main.py           # FastAPI app
│   ├── config.py         # Configuration
│   ├── models.py         # Pydantic models
│   ├── evaluator.py      # Core logic
│   ├── openrouter_client.py  # API client
│   └── prompts.py        # System prompts
├── frontend/
│   └── app.py           # Streamlit UI
├── .env                 # API keys
└── README.md
```

## API Usage

**POST /evaluate**
```json
{
  "question": "What is 2+2?"
}
```

**Response:**
```json
{
  "question": "What is 2+2?",
  "answer": "4",
  "evaluation": "Correct",
  "score": 1
}
```

## Models Used

- **Answer Generation**: `openai/gpt-5-nano`
- **Answer Evaluation**: `openai/gpt-4.1-nano`

## Environment Variables

```env
OPENROUTER_API_KEY=your_openrouter_key_here
```