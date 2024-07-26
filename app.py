from tweepy_integration import setup_twitter_client, tweet
from openai_integration import setup_openai, get_reply
from edit_message_history import read_history, write_history
from prompt_constructor import construct_prompt
from gui import setup_gui

isTesting = True

def setup():
    tweepy_client = setup_twitter_client()
    openai_client = setup_openai()
    # setup_gui()
    file_path = "message_history.txt"
    
    return tweepy_client, openai_client, file_path

def main():
    tweepy_client, openai_client, file_path = setup()
    history = read_history(file_path)
    message, behaviour = construct_prompt(history)
    if not isTesting:
        content = get_reply(openai_client, message, behaviour)
        write_history(file_path, content)
        print("content:" + content)
        # tweet(tweepy_client, content)
        # print("not testing")
    else:
        print("testing")
        print(message)
        print("\n")
        print(behaviour)
        content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        write_history(file_path, content)

if __name__ == "__main__":
    main()