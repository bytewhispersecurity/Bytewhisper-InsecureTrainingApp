import os, re
import json
from datetime import datetime

# This function will log the chat messages to a file
def log_chat(user_message: str, system_message: str, output_message: str):
    # Create a directory for logs if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a log file with the current date
    log_file = f'logs/chat_log_{datetime.now().strftime("%Y-%m-%d")}.log'

    # Initialize the log file if it doesn't exist
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            json.dump([], f, indent=4)

    # Log the messages to the file
    with open(log_file, 'r') as f:
        log_content = json.load(f)
        log_message = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "system_prompt": system_message,
            "user_prompt": user_message,
            "output_message": output_message,
        }
        log_content.append(log_message)
    
    with open(log_file, 'w') as f:
        json.dump(log_content, f, indent=4)
        
        
# This function will return log contents to web UI
def parse_logs():
    log_file = f'logs/chat_log_{datetime.now().strftime("%Y-%m-%d")}.log'

    log_contents = []

    with open(log_file, 'r') as f:
        log = json.load(f)
        for entry in log:
            log_contents.append({
                "timestamp": entry["timestamp"],
                "system_prompt": entry["system_prompt"],
                "user_prompt": entry["user_prompt"],
                "output_message": entry["output_message"],
            })
    
    return log_contents
