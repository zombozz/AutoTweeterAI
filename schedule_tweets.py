import os
import subprocess
from config import exe_in_root

def schedule_task(frequency, day, time):
    task_name = "ScheduledAutoTweeterAI"
    if exe_in_root:
        exe_path = os.path.abspath(os.path.dirname(__file__))
    else:
        exe_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist')
    exe_file = os.path.join(exe_path, 'app.exe')  # Name of the executable
    if frequency == 'weekly':
        cmd = f'schtasks /create /tn {task_name} /tr "{exe_file}" /sc {frequency} /d {day} /st {time}'
    elif frequency == 'daily':
        cmd = f'schtasks /create /tn {task_name} /tr "{exe_file}" /sc {frequency} /st {time}'
    elif frequency == 'hourly':
        cmd = f'schtasks /create /tn {task_name} /tr "{exe_file}" /sc {frequency} /mo 1'

    # try:
    #     subprocess.run(cmd, check=True, shell=True)
    #     return(f"Task '{task_name}' scheduled successfully.")
    # except subprocess.CalledProcessError as e:
    #     return(f"Failed to schedule task. Error: {e}")
    return(cmd)
