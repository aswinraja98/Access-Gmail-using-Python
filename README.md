Email Inbox Parser
This Python script fetches unseen emails from a Gmail inbox using IMAP, extracts relevant information such as subject, sender, recipient, and date, along with the email body and HTML content if available, and stores them in a list of dictionaries.

Requirements
Python 3.x
imaplib (standard library)
email (standard library)
Usage
Clone this repository:

git clone https://github.com/your_username/email-inbox-parser.git
Navigate to the project directory:

cd email-inbox-parser
Modify the username and password variables in the script (inbox_parser.py) to your Gmail credentials.

Run the script:

python inbox_parser.py
Script Explanation
inbox_parser.py: This is the main script that fetches unseen emails from your Gmail inbox using IMAP, extracts relevant information, and prints them.
Note
Ensure that IMAP is enabled in your Gmail settings.
It's recommended to use an application-specific password instead of your main Google account password for security reasons.
Disclaimer
This script is provided as-is without any warranties. Use it responsibly and at your own risk.
