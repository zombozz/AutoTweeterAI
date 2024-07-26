import PySimpleGUI as sg
from config import Config
from make_logs import log_message
from tweepy_integration import setup_twitter_api, setup_twitter_client, tweet
from openai_integration import setup_openai, verify_openai_key, get_reply
from prompt_constructor import construct_prompt
from edit_message_history import read_history, write_history
from schedule_tweets import get_current_schedule, schedule_task

def setup_gui():
    sg.theme('Dark Grey 10')
    layout = [
        [sg.Text("Enter Twitter API Details.")],
        [sg.Text('API Key:'), sg.Input(key='-TWITTER_API_KEY-')],
        [sg.Text('API Secret Key:'), sg.Input(key='-TWITTER_API_SECRET-')],
        [sg.Text('Access Token:'), sg.Input(key='-TWITTER_ACCESS_TOKEN-')],
        [sg.Text('Access Token Secret:'), sg.Input(key='-TWITTER_ACCESS_TOKEN_SECRET-')],
        [sg.Text('OpenAI API Key:'), sg.Input(key='-OPENAI_API_KEY-')],
        [sg.Button('Update API Details'), sg.Button("I've done this already"), sg.Button('Exit')]
    ]

    window = sg.Window('API Details', layout, size=(400, 300), resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            return None
        
        if event == 'Update API Details':
            api_details = {
                'TWITTER_API_KEY': values['-TWITTER_API_KEY-'],
                'TWITTER_API_SECRET': values['-TWITTER_API_SECRET-'],
                'TWITTER_ACCESS_TOKEN': values['-TWITTER_ACCESS_TOKEN-'],
                'TWITTER_ACCESS_TOKEN_SECRET': values['-TWITTER_ACCESS_TOKEN_SECRET-'],
                'OPENAI_API_KEY': values['-OPENAI_API_KEY-']
            }
            save_keys(api_details)
            pass

        if setup_twitter_api():
            if verify_openai_key():
                # sg.popup("API details verified successfully.")
                tweepy_client = setup_twitter_client()
                openai_client = setup_openai()
                return tweepy_client, openai_client
            else:
                sg.popup('Your OpenAI API Key could not be verified.')
        else:
            sg.popup('Your Twitter API Keys could not be verified.')


def tweet_config_gui(tweepy_client, openai_client):
    layout = [
        [sg.Text('Configure Tweet Settings')],
        [sg.Text('History Context Option:'), sg.Combo(['1', '2'], key='-HISTORY_OPTION-')],
        [sg.Text("Option 1: Write USING previous messages for context.", size=(50, None), auto_size_text=True)],
        [sg.Text("Option 2: Don't use message history as context", size=(50, None), auto_size_text=True)],
        [sg.Text('Prompt:'), sg.Input(key='-PROMPT-')],
        [sg.Text('Persona:'), sg.Input(key='-PERSONA-')],
        [sg.Text('Use Behaviour:'), sg.Input(key='-USE_BEHAVIOUR-')],
        [sg.Text('Avoid Behaviour:'), sg.Input(key='-AVOID_BEHAVIOUR-')],
        [sg.Text('Tweet Now or Schedule?')],
        [sg.Button('View Sample Tweet'), sg.Button('Tweet Now')],
        [sg.Button('Schedule Tweet'), sg.Button('Exit')]
    ]

    window = sg.Window('Configure Options', layout, size=(400, 400), resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            return None
        
        if event == 'View Sample Tweet':
            tweet_settings = {
                'USE_HISTORY_CONTEXT_OPTION': values['-HISTORY_OPTION-'],
                'PROMPT': values['-PROMPT-'],
                'PERSONA': values['-PERSONA-'],
                'USE_BEHAVIOUR': values['-USE_BEHAVIOUR-'],
                'AVOID_BEHAVIOUR': values['-AVOID_BEHAVIOUR-'],
            }
            save_keys(tweet_settings)
            history_file_path = "message_history.txt"
            history = read_history(history_file_path)
            message, behaviour = construct_prompt(history)
            content = get_reply(openai_client, message, behaviour)
            
            loading_text = "Loading..."
            if '-SAMPLE_TEXT-' in window.AllKeysDict:
                window['-SAMPLE_TEXT-'].update("Loading...")
            else:
                window.extend_layout(window, [[sg.Text(loading_text, size=(50, None), auto_size_text=True, key='-SAMPLE_TEXT-')]])
            window.refresh()
            content = get_reply(openai_client, message, behaviour)
            window['-SAMPLE_TEXT-'].update(content)
            pass

        if event == 'Tweet Now':
            tweet(tweepy_client, content)
            write_history(history_file_path, content)
            sg.popup("Tweeted OK")

        if event == 'Schedule Tweet':
            layout = [
                [sg.Text('Select Frequency')],
                [sg.Combo(['Daily', 'Weekly', 'Hourly'], key='-FREQUENCY-')],
                [sg.Text('For Weekly, select Day:'), sg.Combo(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'], key='-DAY-')],
                [sg.Text('Enter Time (HH:MM):'), sg.Input(key='-TIME-')],
                [sg.Button('Confirm Schedule'), sg.Button('Back')],
                [sg.Text(get_current_schedule())]
            ]

            schedule_window = sg.Window('Schedule Tweet', layout, size=(400, 300), resizable=True)

            while True:
                event, values = schedule_window.read()
                if event in (sg.WIN_CLOSED, 'Back'):
                    schedule_window.close()
                    break 

                if event == 'Confirm Schedule':
                    schedule_settings = {
                        'SCHEDULE_FREQUENCY': values['-FREQUENCY-'],
                        'SCHEDULE_DAY': values['-DAY-'],
                        'SCHEDULE_TIME': values['-TIME-']
                    }
                    save_keys(schedule_settings)
                    schedule_task()
                    schedule_window.close()
                    break

def save_keys(details_keys):
    config = Config()
    updates = {}
    for key, value in details_keys.items():
        if value.strip():  
            updates[key] = value
    
    if updates:
        config.update_json(**updates)
        log_message("Updated details in config.json file.")
    else:
        log_message("No details were updated in config.json as all values were empty.")

