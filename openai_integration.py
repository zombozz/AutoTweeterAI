from openai import OpenAI
from config import OPENAI_API_KEY

def setup_openai():
    openai_client = OpenAI(api_key = OPENAI_API_KEY)
    return openai_client

def get_reply(openai_client, message_to_ai, ai_rules):
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=
            [
                {"role": "system", "content": ai_rules},
                {"role":"user", "content": message_to_ai},
            ]
    )
    content = response.choices[0].message.content
    return content