"""
Demo script demonstrating API key usage with a dummy secret key.
NOTE: Never commit real secret keys into source code or version control.
"""

import os

# Dummy API Key for demonstration / testing purposes
API_KEY = os.getenv("API_KEY", "")
API_SECRET = os.getenv("API_SECRET", "")

def call_mock_api(endpoint: str, payload: dict | None = None):
    """
    Simulates making an authenticated API request with the dummy credentials.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-API-Secret": API_SECRET,
        "Content-Type": "application/json",
    }
    
    masked_key = f"{API_KEY[:10]}...{API_KEY[-4:]}"
    print(f"[Request] Sending request to {endpoint}")
    print(f"[Headers] Authorization: Bearer {masked_key}")
    
    # Simulated response
    return {
        "status": 200,
        "message": "Authenticated request simulated successfully",
        "endpoint": endpoint,
        "data": payload or {}
    }


if __name__ == "__main__":
    print("--- Running API Key Demo ---")
    response = call_mock_api("/v1/transactions", {"amount": 100, "currency": "USD"})
    print("Response:", response)
