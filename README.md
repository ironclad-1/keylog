Version: 1.0.0
Date: 12th March,2025.
Author: SHAIK ASHRAAF

Overview

This repository contains a Python-based KEYlogger designed for monitoring employee activities on company-issued laptops. The system continuously logs keystrokes, stores them securely, and sends encrypted logs to a remote server via Telegram for monitoring purposes. The script is designed to be run in the background with minimal interaction from the user, ensuring that it remains invisible while performing its tasks.

This tool is intended for ethical use under the supervision of the company’s HR and ethical boards. The project is hypothetical and not intended for illegal use or deployment without explicit consent.

Features

Keystroke Logging: The system logs each keystroke typed on the laptop, capturing timestamps and key events.
Telegram Integration: Logs are sent to a Telegram bot in real time for monitoring purposes, enabling remote observation of employee activities.
Automatic Log Flush: Logs are temporarily stored in memory, and once a certain buffer size is reached, they are flushed to a log file for persistent storage.
Log Encryption: Logs are encrypted using the Fernet encryption method to ensure secure storage, preventing unauthorized access.
Background Operation: The script runs continuously in the background, without user interaction, to ensure that it remains unobtrusive.
Data Cleanup: The script includes a stealth cleanup feature that periodically sends logs to the Telegram bot, and after transmission, the logs are encrypted and securely stored.
Persistent Monitoring: The system operates indefinitely, continuing to monitor keystrokes and send logs until it is manually stopped or terminated under controlled conditions.

Installation Instructions
Requirements:
Python 3.x

Install the necessary dependencies using:
pip install -r requirements.txt
Libraries include: keyboard, requests, cryptography, python-dotenv

Setup:
Clone the repository to your local machine:

Configure Telegram Bot:
Obtain your Telegram Bot API Token from the BotFather and set it in your .env file:

Bot_t= your_bot_token_here
Chat_id= your_chat_id_here

Run the Script:
After configuring your environment and installing dependencies, simply run the script:

python teltest.py

The script will run in the background, logging keystrokes and sending them to the specified Telegram chat.

Security & Privacy
Encryption: Logs are encrypted using Fernet encryption to prevent unauthorized access.

Confidentiality: Logs are only sent to a secure Telegram bot, ensuring that sensitive information is handled appropriately.

Compliance: This tool is designed to be used ethically and in compliance with company policies. It must only be deployed in environments where employees have been informed and consented.

Known Limitations
Detection: While the script operates stealthily, there is always a risk that advanced security software might detect and flag its presence.

Permissions: The script requires administrative privileges to run, especially for background tasks and keylogging operations.

Environment: The script may require environment-specific adjustments, particularly when running on different operating systems or configurations.

Future Enhancements
Real-Time Monitoring: Future releases may include additional real-time monitoring capabilities, such as tracking application usage or web activity.

Enhanced Stealth Features: Ongoing improvements to make the script even less detectable by security software.

Alerting System: Integrating automatic alerts for unusual activity or keywords detected in keystrokes.

Disclaimer
This project is intended for hypothetical use only. Unauthorized use is prohibited. All data collected must be handled in accordance with company policies, employee consent, and applicable legal standards.
