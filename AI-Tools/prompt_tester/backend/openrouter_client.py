import requests
from config import OPENROUTER_API_KEY, OPENROUTER_URL


def call_model(model, messages):
    """Call OpenRouter API with the specified model and messages."""
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if "error" in result:
            raise Exception(f"API Error: {result['error']}")
        
        content = result["choices"][0]["message"]["content"]
        
        if content is None:
            raise Exception("API returned empty content")
            
        return content.strip()
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")
    except KeyError as e:
        raise Exception(f"Unexpected API response format: {str(e)}")
    except Exception as e:
        raise Exception(f"API call failed: {str(e)}")