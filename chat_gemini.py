from dotenv import load_dotenv
import os
import json
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# Check cache
if os.path.exists("response_cache.json"):
    with open("response_cache.json", "r") as f:
        cached = json.load(f)
    print("Gemini Response (cached):", cached["text"])
else:
    # Generate response
    response = model.generate_content("Why is the sky blue?")
    # Cache response
    with open("response_cache.json", "w") as f:
        json.dump({"text": response.text}, f)
    print("Gemini Response:", response.text)
