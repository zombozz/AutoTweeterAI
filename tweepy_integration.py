import tweepy
from config import Config

def setup_twitter_api():
    config = Config()
    auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
        return True
    except:
        print("Error during authentication")
        return False

def setup_twitter_client():
    config = Config()
    tweepy_client = tweepy.Client(
        consumer_key=config.TWITTER_API_KEY,
        consumer_secret=config.TWITTER_API_SECRET,
        access_token=config.TWITTER_ACCESS_TOKEN,
        access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET
    )
    return tweepy_client

def tweet(tweepy_client, content):
    tweepy_client.create_tweet(text=content)
