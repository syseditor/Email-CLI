# A dumb for any methods used in email-cli.py

import ssl
import time
import smtplib

from email.mime.text import MIMEText

from decoration import *

port = 465

def send_email(sender: str, password: str, recipient: str, subject: str, content: str): # Sends the email
    context = ssl.create_default_context()

    message = MIMEText(content)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    print(f"{wait} {color['t-pink']}Logging in...{reset}")
    cursor('up', 1)
    cursor('right', 19)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        try:
            server.login(sender, password)
            clear_line()
            print(f"{notice} {color['t-pink']}Successful login!{reset}")
            time.sleep(1)
            cursor('up', 1)
            clear_line()
            print(f"{wait} {color['t-pink']}Sending email to {recipient}{reset}")
            time.sleep(0.5)
            server.send_message(message)
            cursor('up', 1)
            clear_line()
            print(f"{notice} {color['t-pink']}Successfully sent the email!{reset}")
            time.sleep(1)
            result = 0
            cursor('up', 1)
            clear_line()
        except Exception as e:
            clear_line()
            print(f"{warning} {color['t-green']}{style['bold']}{style['underline']}Error{reset}{color['t-green']}: {color['magenta']}{e}{reset}")
            result = 1
        finally:
            print(f"{wait} {color['t-pink']}Logging out...{reset}")
            cursor('up', 1)
            server.quit()
            clear_line()
            print(f"{notice} {color['t-pink']}Successful logout!{reset}")
            time.sleep(0.5)
            cursor('up', 1)
    
    return result