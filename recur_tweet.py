import os
from tweepy_integration import setup_twitter_client, tweet
from openai_integration import setup_openai, get_reply
from prompt_constructor import construct_prompt
from edit_message_history import read_history, write_history

def main():
    try:
        tweepy_client = setup_twitter_client()
        openai_client = setup_openai()
        history_file_path = "message_history.txt"
        history = read_history(history_file_path)
        message, behaviour = construct_prompt(history)
        content = get_reply(openai_client, message, behaviour)
        print(content)
        tweet(tweepy_client, content)

        write_history(history_file_path, content)
        
    
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
