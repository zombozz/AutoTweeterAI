from make_logs import log_message
# from schedule_tweets import testFP
from gui import setup_gui, tweet_config_gui

isTesting = False

def main():
    try:
        tweepy_client, openai_client = setup_gui()
        tweet_config_gui(tweepy_client, openai_client)
        print("not testing")

    except Exception as e:
        log_message(f"Error in main function: {e}")


if __name__ == "__main__":
    log_message("Script started.")
    main()
    log_message("Script finished.")