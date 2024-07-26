from datetime import datetime

def log_message(message):
    with open('script_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
        log_file.write(f"{message}\n")