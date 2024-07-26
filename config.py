from dotenv import load_dotenv
import os
load_dotenv()

#Replace each 'KEY' text with your own corresponding API keys. 4 from X (Twitter) and 1 from OpenAI respectively. See Repo for more info.
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

#Configure Open AI input by editing the values in the "" below:
prompt = "pretend you're a senile old man yapping to kids abou tthe good old days"
persona = "witty, cool"
use_behaviour = "1 or 2 emojis"
avoid_behaviour = "repeating things similar to previous replies"

#Configure Open AI input using message history (message_history.txt file) as context by changing the number below:
    #1 = Avoid using previous messages as context i.e. come up with something UNIQUE and DIFFERENT to previous/given messages.
    #2 = Use previous messages as context i.e. come up with something SIMILAR to previous messages
    #3 = Don't send AI previous messages as context
use_history_context_option = 1

#Leave this alone
exe_in_root = False