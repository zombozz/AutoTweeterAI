# AutoTweeterAI

## Overview

This Python-based tool integrates Twitter with OpenAI's GPT-4 model to automate tweet generation and scheduling. It manages Twitter API interactions using Tweepy and uses GPT-4 to generate content based on historical messages. The tool features a graphical user interface (GUI) built with PySimpleGUI, allowing users to configure Twitter API details, tweet settings, and scheduling options. It supports dynamic configuration updates and saves settings for persistent usage.

This is a more of a personal project to attempy growing my Twitter account without actually using Twitter (I don't like Twitter) so it's not really designed as user friendly as it could possibly be. This will require you to generate your own Twitter and OpenAI API keys (sorry you can't have mine🤪): 
Generate Twitter API Keys: https://developer.x.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
**Note that you'll need both Read and Write permissions**
Generate OpenAI API Key: https://platform.openai.com/docs/quickstart

Once you've got those though, it's pretty easy to use, but I might be biased. Let me know if you need any help or have any questions!


## Features

- **Twitter API Integration**: Easily configure and manage Twitter API keys and tokens.
- **AI Prompt Configuration**: Set up AI settings, including prompt, persona, and behavior rules.
- **Scheduling Options**: Schedule tweets with flexible timing and frequency options.
- **Message History Management**: Maintain and use message history to enhance AI-generated content and context.
- **Persistent Configuration**: Save and load settings from configuration files for persistent usage.
- **GUI Interface**: Intuitive and user-friendly interface for configuring and managing Twitter interactions.

## Components

- **`config.py`**: Manages configuration using a JSON file. Handles loading and updating of settings including API keys and scheduling options.
- **`tweepy_integration.py`**: Handles Twitter API interactions for posting tweets and authenticating credentials.
- **`openai_integration.py`**: Interfaces with OpenAI's API to generate content based on prompts and historical messages.
- **`edit_message_history.py`**: Manages reading and writing of message history.
- **`prompt_constructor.py`**: Constructs prompts for OpenAI based on historical messages.
- **`schedule_tweets.py`**: Schedules tweets based on configured frequency and timing.
- **`make_logs.py`**: Handles logging of messages and errors.
- **`gui.py`**: Provides a graphical interface for users to update API details and settings.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/zombozz/AutoTweeterAI.git
   cd AutoTweeterAI
   
2. **Run Exe File**:
    ```bash
    cd dist
    ./app.exe
    
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


