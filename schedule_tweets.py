import os
import subprocess
from config import Config
from make_logs import log_message
import sys

def get_current_schedule():
    config = Config()
    frequency = config.schedule_frequency.capitalize()
    day = config.schedule_day.upper() if config.schedule_frequency.lower() == 'weekly' else 'N/A'
    time = config.schedule_time

    return f"Frequency: {frequency}\nDay: {day}\nTime: {time}"

def schedule_task():
    config = Config()
    frequency = config.schedule_frequency
    day = config.schedule_day
    time = config.schedule_time

    task_name = "ScheduledAutoTweeterAI"

    # if config.exe_in_root == True:
    #     print("config exe in root")
    #     exe_path = os.path.dirname(os.path.abspath(__file__))
    #     log_message(exe_path)
    # else:
    #     print("config exe NOT in root")
    #     exe_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist')

    if getattr(sys, 'frozen', False):
        # If the application is frozen, get the path to the executable
        exe_path = os.path.dirname(sys.executable)
    else:
        # If the application is not frozen, get the path to the current script
        exe_path = os.path.dirname(os.path.abspath(__file__))

    exe_file = os.path.join(exe_path, 'recur_tweet.exe')
    log_message(exe_file)

    if frequency == 'Weekly':
        cmd = f'schtasks /create /tn {task_name} /tr "{exe_file}" /sc weekly /d {day} /st {time}'
    elif frequency == 'Daily':
        cmd = f'schtasks /create /tn {task_name} /tr "{exe_file}" /sc daily /st {time}'
    elif frequency == 'Hourly':
        cmd = f'schtasks /create /tn {task_name} /tr "{exe_file}" /sc hourly /mo 1'

    print("cmd" + cmd)
    try:
        subprocess.run(cmd, check=True, shell=True)
        log_message(f"Task '{task_name}' scheduled successfully.")
        return(f"Task '{task_name}' scheduled successfully.")
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to schedule task. Error: {e}")
        return(f"Failed to schedule task. Error: {e}")
