import smtplib, json
from email.mime.text import MIMEText


class EmailSendor :
    def __init__(self, setting_path = "secrets/account.json"):
        with open(setting_path) as json_file : 
            json_data = json.load(json_file)
            json_data = json_data["smtp"]["google"]
            
            self.smtp_server = json_data["smtp_server"]
            self.smtp_port = json_data["smtp_port"]
            self.sender_email = json_data["sender_email"]
            self.sender_password = json_data["sender_password"]
        
    def send(self, send_to, title, message) :
        message = MIMEText(message)
        message['Subject'] = title
        message['From'] = self.sender_email
        message['To'] = send_to

        # 이메일 전송
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, send_to, message.as_string())        
