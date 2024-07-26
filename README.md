# AutoTweeterAI

## Overview

This Python-based tool integrates Twitter with OpenAI's GPT-4 model to automate tweet generation and scheduling. It manages Twitter API interactions using Tweepy and uses GPT-4 to generate content based on historical messages. The tool features a graphical user interface (GUI) built with PySimpleGUI, allowing users to configure Twitter API details, tweet settings, and scheduling options. It supports dynamic configuration updates and saves settings for persistent usage.

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


