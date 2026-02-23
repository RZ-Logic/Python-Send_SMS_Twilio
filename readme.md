# Twilio SMS Automation

A lightweight, reusable Python utility for automating SMS notifications via the Twilio API. This script allows you to easily send text messages to individual numbers or broadcast alerts to multiple recipients simultaneously directly from the command line.

## 🚀 Features

* **Single & Bulk Messaging:** Send an SMS to one number or pass a space-separated list of numbers to broadcast to a group.
* **Modular Design:** Separates the command-line interface (`send_sms.py`) from the core Twilio logic (`sms_helper.py`) for easy integration into larger automation projects or agentic workflows.
* **Secure Configuration:** Uses environment variables to manage sensitive Twilio credentials securely.

## 📋 Prerequisites

Before running the script, ensure you have the following:

1.  Python 3.x installed.
2.  A [Twilio](https://www.twilio.com/) account with an active phone number capable of sending SMS.
3.  The Twilio Python helper library installed:
    ```bash
    pip install twilio
    ```

## ⚙️ Configuration

The script relies on environment variables to authenticate with Twilio. You must set the following variables in your environment before running the script:

* `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
* `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
* `TWILIO_FROM_NUMBER`: Your Twilio phone number (e.g., `+12345678900`).

**On macOS/Linux:**
```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_FROM_NUMBER="+12345678900"
```

On Windows (Command Prompt):
```
set TWILIO_ACCOUNT_SID=your_account_sid
set TWILIO_AUTH_TOKEN=your_auth_token
set TWILIO_FROM_NUMBER=+12345678900
```

💻 Usage
Run the script from the command line using the following syntax:

`python send_sms.py "<to_number(s)>" "<message>"`

Examples
1. Sending to a single number:

`python send_sms.py "+14155551234" "Hello from Python automation!"`

2. Broadcasting to multiple numbers:
Enclose the list of space-separated E.164 formatted numbers in quotes.

`python send_sms.py "+19059999999 +14155551234 +6471234567" "Group alert: The automated system has finished processing."`

📁 File Structure

`send_sms.py`: The main executable script that parses command-line arguments and passes them to the helper function.

`sms_helper.py`: Contains the _get_client() authentication logic and the send_sms() function that interacts with the Twilio REST API.
