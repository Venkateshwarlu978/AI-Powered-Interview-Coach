import google.generativeai as genai
import os
from dotenv import load_dotenv  # Fixed typo from loaddotenv to load_dotenv

# Load environment variables
load_dotenv()

# Use the EXACT name from your .env file
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    print("API Key loaded successfully!")
else:
    print("Check your .env file—Python still can't see GEMINI_API_KEY")

# Use the correct working model
model = genai.GenerativeModel("gemini-3-flash-preview")

def generate_question(role):
    """Generate an interview question for the specified role."""
    try:
        response = model.generate_content(
            f"Ask one interview question for a {role} role."
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def evaluate_answer(question, answer):
    """Evaluate the provided answer to a question."""
    try:
        response = model.generate_content(f"""
        Question: {question}
        Answer: {answer}

        Evaluate and give:
        - Technical Accuracy (out of 10)
        - Grammar (out of 10)
        - Confidence (out of 10)
        - Strengths
        - Weaknesses
        """)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
