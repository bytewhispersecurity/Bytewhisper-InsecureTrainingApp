import os
from datetime import datetime

# This function will log the chat messages to a file
def log_chat(user_message: str, system_message: str, output_message: str, risk_score: int):
    # Create a directory for logs if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a log file with the current date
    log_file = f'logs/chat_log_{datetime.now().strftime("%Y-%m-%d")}.log'

    # Log the messages to the file
    with open(log_file, 'a') as f:
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"System Prompt: {system_message}\n")
        f.write(f"User Prompt: {user_message}\n")
        f.write(f"Prompt Output: {output_message}\n")
        f.write(f"Risk Score: {risk_score}\n")
        f.write("\n")