from google import genai
from config import key
import json

client = genai.Client(
        api_key=key
    )

def get_tasks(msg):
    example_json = """
        {
            "task1": "Find current AI healthcare trends",
            "task2": "Find real-world healthcare AI examples",
            "task3": "Identify risks and challenges",
            "task4": "Generate final summary"
        }
        """
    prompt = f"""
        You are a Planner Agent.

        Your job is to break a user request into smaller executable tasks.

        Rules:
        1. Return ONLY in json format.
        2. Each item must be a string.
        3. No explanations.
        4. No markdown.
        5. No code fences.
        6. No extra text.
        7. If the task is about any mathematical calculations, for eg: calculate 4*7, then return calc 4*7. always return in this format

        Example:

        User:
        Research the impact of AI in healthcare and give me:
        1. Key trends
        2. 3 real-world examples
        3. Risks
        4. Final summary

        Output:
        {example_json}

        User:
        {msg}
        """
    
    
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    return json.loads(response.text)
    
