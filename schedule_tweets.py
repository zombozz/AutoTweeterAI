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
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    else:
        exe_path = os.path.dirname(os.path.abspath(__file__))

    cmd = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c cd /d {exe_path} && recur_tweet.exe"'

    if frequency == 'Weekly':
        cmd += f' /sc weekly /d {day} /st {time}'
    elif frequency == 'Daily':
        cmd += f' /sc daily /st {time}'
    elif frequency == 'Hourly':
        cmd += ' /sc hourly /mo 1'
    print("cmd" + cmd)
    try:
        subprocess.run(cmd, check=True, shell=True)
        log_message(f"Task '{task_name}' scheduled successfully.")
        return(f"Task '{task_name}' scheduled successfully.")
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to schedule task. Error: {e}")
        return(f"Failed to schedule task. Error: {e}")
    

def testFP():
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
    else:
        exe_path = os.path.dirname(os.path.abspath(__file__))

    exe_file = os.path.join(exe_path, 'recur_tweet.exe')
    log_message(exe_file)
