import PySimpleGUI as sg

def setup_gui():
    # Step 1: API Details
    layout = [
        [sg.Text('Enter Twitter API Details')],
        [sg.Text('API Key:'), sg.Input(key='-TWITTER_API_KEY-')],
        [sg.Text('API Secret Key:'), sg.Input(key='-TWITTER_API_SECRET-')],
        [sg.Text('Access Token:'), sg.Input(key='-TWITTER_ACCESS_TOKEN-')],
        [sg.Text('Access Token Secret:'), sg.Input(key='-TWITTER_ACCESS_TOKEN_SECRET-')],
        [sg.Button('Confirm API Details'), sg.Button('Exit')]
    ]

    window = sg.Window('API Details', layout, size=(400, 300), resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            return None  # Exit if user chooses to close or exit
        
        if event == 'Confirm API Details':
            # Validate and store the API keys
            break

    window.close()

    # Step 2: Configure Options
    layout = [
        [sg.Text('Configure Tweet Settings')],
        [sg.Text('History Context Option:'), sg.Combo(['1', '2', '3'], key='-HISTORY_OPTION-')],
        [sg.Text('Prompt:'), sg.Input(key='-PROMPT-')],
        [sg.Text('Persona:'), sg.Input(key='-PERSONA-')],
        [sg.Text('Use Behaviour:'), sg.Input(key='-USE_BEHAVIOUR-')],
        [sg.Text('Avoid Behaviour:'), sg.Input(key='-AVOID_BEHAVIOUR-')],
        [sg.Text('Tweet Now or Schedule?')],
        [sg.Button('Tweet Now'), sg.Button('Schedule Tweet')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Configure Options', layout, size=(400, 400), resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            return None  # Exit if user chooses to close or exit

        if event == 'Tweet Now':
            # Handle tweet now logic
            # Call your tweet function here
            break

        if event == 'Schedule Tweet':
            # Step 3: Scheduling Options
            layout = [
                [sg.Text('Select Frequency')],
                [sg.Combo(['Daily', 'Weekly', 'Hourly'], key='-FREQUENCY-')],
                [sg.Text('For Weekly, select Day:'), sg.Combo(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'], key='-DAY-')],
                [sg.Text('Enter Time (HH:MM):'), sg.Input(key='-TIME-')],
                [sg.Button('Confirm Schedule'), sg.Button('Back')]
            ]

            window = sg.Window('Schedule Tweet', layout, size=(400, 300), resizable=True)

            while True:
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'Back'):
                    window.close()
                    break  # Go back to configure options

                if event == 'Confirm Schedule':
                    # Handle scheduling logic
                    # Call your schedule_task function here
                    window.close()
                    break

    window.close()

# Call the setup_gui function to start the GUI
if __name__ == "__main__":
    setup_gui()
