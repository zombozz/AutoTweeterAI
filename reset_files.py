import os
import json

def reset_file(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)

def reset_config(file_path):
    default_config = {
        "TWITTER_API_KEY": "",
        "TWITTER_API_SECRET": "",
        "TWITTER_ACCESS_TOKEN": "",
        "TWITTER_ACCESS_TOKEN_SECRET": "",
        "OPENAI_API_KEY": "",
        "PROMPT": "write a first person message about how much you love coding",
        "PERSONA": "tired",
        "USE_BEHAVIOUR": "first person",
        "AVOID_BEHAVIOUR": "robotic",
        "USE_HISTORY_CONTEXT_OPTION": "2",
        "SCHEDULE_FREQUENCY": "Daily",
        "SCHEDULE_DAY": "MON",
        "SCHEDULE_TIME": "09:40",
        "EXE_IN_ROOT": "True"
    }
    with open(file_path, 'w') as file:
        json.dump(default_config, file, indent=4)

def reset_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(current_dir, 'dist')

    files_to_reset = ['script_log.txt', 'message_history.txt']
    config_file = 'config.json'

    # Reset files in the current directory
    for file_name in files_to_reset:
        reset_file(os.path.join(current_dir, file_name))

    reset_config(os.path.join(current_dir, config_file))

    # Reset files in the dist directory
    if os.path.exists(dist_dir):
        for file_name in files_to_reset:
            reset_file(os.path.join(dist_dir, file_name))
        
        reset_config(os.path.join(dist_dir, config_file))

if __name__ == "__main__":
    reset_files()
