import email, smtplib, ssl
from providers import PROVIDERS
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

personalEmail = os.getenv("personal_email")
appPassword = os.getenv("googleAppKey")
phoneNumber = os.getenv("phoneNumber")


def send_sms_via_email(number:str, 
                       message:str, 
                       provider:str, 
                       sender_credentials:tuple, 
                       subject:str="sent using python", 
                       smtp_server="smtp.gmail.com", 
                       smtp_port:int = 465):
    sender_email, email_password = sender_credentials
    receiver_email=f"{number}@txt.att.net"

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def main():
    number = phoneNumber
    message = "Hi bro."
    provider = "AT&T"
    sender_credentials = (personalEmail,appPassword)

    send_sms_via_email(number, message, provider, sender_credentials)

if __name__ == "__main__":
    main()

