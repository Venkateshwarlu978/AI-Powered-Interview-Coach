INTERVIEW_PROMPT = """
You are an expert interviewer for the role of {role}.
Ask one interview question at a time.
"""

EVALUATION_PROMPT = """
Evaluate the candidate's answer.

Question: {question}
Answer: {answer}

Give:
1. Technical Accuracy (out of 10)
2. Grammar Score (out of 10)
3. Confidence Score (out of 10)
4. Strengths
5. Weaknesses
6. Final suggestion

Return in clean structured format.
"""