from tweepy_integration import setup_twitter_client, tweet
from openai_integration import setup_openai, get_reply
from gui import setup_gui

def main():
    tweepy_client = setup_twitter_client()
    openai_client = setup_openai()
    setup_gui()

    # content = get_reply(openai_client, "write a short message about how cool coding is", "respond in 20 words or less")
    # tweet(tweepy_client, content)

if __name__ == "__main__":
    main()