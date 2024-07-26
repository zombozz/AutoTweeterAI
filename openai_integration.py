from openai import OpenAI
from config import Config
from make_logs import log_message

def setup_openai():
    config = Config()
    openai_client = OpenAI(api_key = config.OPENAI_API_KEY)
    return openai_client

def verify_openai_key():
    config = Config()
    openai_client = OpenAI(api_key = config.OPENAI_API_KEY)
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=
                [
                    {"role": "system", "content": "hi"},
                    {"role":"user", "content": "hi"},
                ]
        )
        log_message("openai wokrs")
        return True
    except Exception as e:
        log_message(f"An error occurred: {e}")
        return False

def get_reply(openai_client, message_to_ai, ai_rules):
    try:

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
    except Exception as e:
        log_message(f"Error in openai function: {e}")
        return 0