# Version: 1.0.0
**Date**: 12th March,2025.
<br />**Author**: SHAIK ASHRAAF

# Overview

This repository contains a Python-based KEYlogger designed for monitoring keyboard activities on a computer. The system continuously logs keystrokes, stores them securely, and sends encrypted logs to a remote server via Telegram. The script is designed to be run in the background with minimal interaction from the user, ensuring that it remains invisible while performing its tasks.

***This tool is intended for ethical use under supervision. The project is hypothetical and not intended for illegal use or deployment without explicit consent.***

# Features

**Keystroke Logging**: The system logs each keystroke typed on the laptop, capturing timestamps and key events.
<br />**Telegram Integration**: Logs are sent to a Telegram bot in real time for monitoring purposes, enabling remote observation of employee activities.
<br />**Automatic Log Flush**: Logs are temporarily stored in memory, and once a certain buffer size is reached, they are flushed to a log file for persistent storage.
<br />**Log Encryption**: Logs are encrypted using the Fernet encryption method to ensure secure storage, preventing unauthorized access.
<br />**Background Operation**: The script runs continuously in the background, without user interaction, to ensure that it remains unobtrusive.
<br />**Data Cleanup**: The script includes a stealth cleanup feature that periodically sends logs to the Telegram bot, and after transmission, the logs are encrypted and securely stored.
<br />**Persistent Monitoring**: The system operates indefinitely, continuing to monitor keystrokes and send logs until it is manually stopped or terminated under controlled conditions.

### Installation Instructions
Requirements:
- Python 3.x

Install the necessary dependencies using:
  
- Libraries include: keyboard, requests, cryptography, python-dotenv

### Setup:   
**Clone the repository to your local machine:**

    git clone   https://github.com/ironclad-1/keylog/tree/main
   
**Configure Telegram Bot:**

Obtain your Telegram Bot API Token from the **BotFather** and set it in your **.env** file:

    Bot_t = your_bot_token_here
    Chat_id = your_chat_id_here

**Run the Script:**
    
    python teltest.py

The script will run in the background, logging keystrokes and sending them to the specified Telegram chat.

## Security & Privacy
**Encryption**: Logs are encrypted using Fernet encryption to prevent unauthorized access.
<br />**Confidentiality**: Logs are only sent to a secure Telegram bot, ensuring that sensitive information is handled appropriately.
<br />**Compliance**: This tool is designed to be used ethically and in compliance with company policies. It must only be deployed in environments where employees have been informed and consented.

## Known Limitations
*Detection*: While the script operates stealthily, there is always a risk that advanced security software might detect and flag its presence.
<br />*Permissions*: 
The script requires administrative privileges to run, especially for background tasks and keylogging operations.
<br />*Environment*: The script may require environment-specific adjustments, particularly when running on different operating systems or configurations.


## Disclaimer
This project is intended for educational purpose / curiosity only. Unauthorized use is prohibited. All data collected must be handled in accordance with consent, and applicable legal standards.
<br /><br />**Note:** The provider of this source code is not responsible for any illegal actions or misuse of the code by individuals or organizations that choose to use it. It is advised to use this code.  It is advised to use this code only in compliance with applicable laws, company policies, and ethical guidelines, ensuring full transparency and consent from all parties involved.
