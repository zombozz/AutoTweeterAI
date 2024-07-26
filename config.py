from dotenv import load_dotenv
import os
load_dotenv()

#Replace each 'KEY' text with your own corresponding API keys. 4 from X (Twitter) and 1 from OpenAI respectively.

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')