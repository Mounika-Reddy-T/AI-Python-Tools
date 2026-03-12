import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Model Configuration
GENERATOR_MODEL = "openai/gpt-5-nano"      # For answer generation
JUDGE_MODEL = "openai/gpt-4.1-nano"       # For answer evaluation

# Validation
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

print(f"✓ Configuration loaded successfully")
print(f"✓ Generator Model: {GENERATOR_MODEL}")
print(f"✓ Judge Model: {JUDGE_MODEL}")