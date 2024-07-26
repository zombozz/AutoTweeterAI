from tweepy_integration import setup_twitter_client, tweet
from openai_integration import setup_openai, get_reply
from edit_message_history import read_history, write_history
from prompt_constructor import construct_prompt
from schedule_tweets import schedule_task
from datetime import datetime
from gui import setup_gui

isTesting = False
#'weekly', 'daily', or 'hourly'
schedule_frequency = 'daily'
#for weekly only
schedule_day = 'MON'
#only for weekly and daily
schedule_time = '9:00'

def setup():
    tweepy_client = setup_twitter_client()
    openai_client = setup_openai()
    setup_gui()
    file_path = "message_history.txt"
    
    return tweepy_client, openai_client, file_path


def main():
    try:
        tweepy_client, openai_client, file_path = setup()
        history = read_history(file_path)
        message, behaviour = construct_prompt(history)
        if not isTesting:
            content = get_reply(openai_client, message, behaviour)
            write_history(file_path, content)
            print("content: " + content)
            # tweet(tweepy_client, content)
            # print("not testing")
            log_message(schedule_task(schedule_frequency, schedule_day, schedule_time))

    except Exception as e:
        log_message(f"Error in main function: {e}")

def log_message(message):
    with open('script_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

if __name__ == "__main__":
    log_message("Script started.")
    main()
    log_message("Script finished.")