import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Use Gemini 1.5 Flash explicitly
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def detect_spam(text: str) -> str:
    prompt = (
        "You are a spam detector.\n"
        "Classify the following text as 'Spam' or 'Not Spam' only. No extra explanation.\n\n"
        f"Text: {text}"
    )
    return generate_response(prompt)

def summarize_text(text: str) -> str:
    prompt = (
        "You are a summarization assistant.\n"
        "Summarize the following content in concise form:\n\n"
        f"{text}"
    )
    return generate_response(prompt)


def extract_named_entities(text: str) -> dict:
    prompt = f"""
    Extract named entities from the following text. Return **only** a valid JSON with keys as entity types like "PERSON", "ORG", "GPE", etc.

    Here is the text:
    {text}

    Return format (no explanation, just JSON):

    {{
    "ORG": ["Zepto"]
    }}
    """

    response = model.generate_content(prompt)
    
    try:
        result_text = response.candidates[0].content.parts[0].text.strip()
        print("🔍 Gemini raw response:", result_text)  # Optional logging
        print("🧠 Gemini raw:", response.candidates[0].content.parts[0].text)
        result_json = json.loads(result_text)  # ✅ Convert string to dict
        return result_json
    except Exception as e:
        return {"error": f"JSON parsing failed: {str(e)}"}