import requests
import numpy as np
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def get_embedding(text):
    # Validate input
    if not text or not text.strip():
        raise ValueError("Input text must be non-empty.")

    # Fetch API key securely
    api_key = os.getenv("EURI_API_KEY")
    if not api_key:
        raise EnvironmentError("EURI_API_KEY not found in environment variables.")

    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "input": text,
        "model": "text-embedding-3-small"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad HTTP codes
        data = response.json()

        # Defensive check for embedding
        if 'data' not in data or not data['data']:
            raise ValueError("API response missing 'data' or embedding list is empty.")

        embedding = np.array(data['data'][0]['embedding'])

        return embedding

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)
    except KeyError:
        print("Error parsing embedding from API response.")
    except Exception as e:
        print("Unexpected error:", e)

    return None  # Fallback
