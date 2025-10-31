import base64

def encode_message(message_bytes: bytes) -> str:
    return base64.urlsafe_b64encode(message_bytes).decode()
