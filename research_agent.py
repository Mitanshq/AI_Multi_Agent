from google import genai
from config import key
client = genai.Client(
    api_key=key
)
def get_response(task):
    prompt = f"""
    you are a professional research agent.
    You will research about the task given by the user
    and return the answer
    User task:
    {task}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    return response.text