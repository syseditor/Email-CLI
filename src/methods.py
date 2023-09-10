# A dumb for any functions used in email-cli.py

import smtplib, ssl

def login(email: str, password: str):
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(email, password)
    except Exception as e:
        print(e)
    finally:
        server.quit()