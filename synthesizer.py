from google import genai
from config import key

client = genai.Client(
    api_key=key
)

def synthesizer(memory: dict):
    prompt = f"""
    You will be given a memory dictionary
    where key = task
    and value = response
    You have to professionally combine all the response and 
    return it to the user.
    No other information should be added by yourself.
    The response should looks natural
    
    Memory:
    {memory}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    return response.text