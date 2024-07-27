import os
from make_logs import log_message
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
        
        log_message("Tweet sent successfully.")
    
    except Exception as e:
        log_message(f"Error in recur_tweet.py: {e}")

if __name__ == "__main__":
    log_message("Recur tweet script started.")
    main()
    log_message("Recur tweet script finished.")
