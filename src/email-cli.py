# Main file - app runner

import os
import time

from methods import *
from decoration import *

def cli():
    system = os.name
    # Cleaning the cli window
    if system == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
    # Welcome message
    print(f'''
                                {color['red']}Welcome to Email-CLI, a CLI used to email people!
                                           {color['magenta']}Credits: syseditor (GitHub)
    ''')

    print(f"{notice} {color['t-pink']}{style['underline']}Respond to the following questions to give the appropriate information to the program\n")
    # Information gathering

    # Sender's email
    sender = input(f"{plus} {color['t-yellow']}Enter your email address: {color['a-green']}")
    cursor('up', 1)
    clear_line()

    # Password
    password = input(f"{plus} {color['t-yellow']}Enter your email's app password: {color['a-green']}")
    cursor('up', 1)
    clear_line()

    # Recipient's email
    recipient = input(f"{plus} {color['t-yellow']}Enter the recipient's email address: {color['a-green']}")
    cursor('up', 1)
    clear_line()

    # Subject
    subject = input(f"{plus} {color['t-yellow']}Enter the subject you are writing for: {color['a-green']}")
    cursor('up', 1)
    clear_line()

    # Content
    content = input(f"{plus} {color['t-yellow']}Enter the email's content: {color['a-green']}")
    cursor('up', 1)
    clear_line()

    cursor('up', 2)
    clear_line()

    # Email preparation
    try:
        result = send_email(sender, password, recipient, subject, content)
    except Exception as e:
        result = 1
        clear_line()
        print(f"{warning} {color['t-green']}{style['bold']}{style['underline']}Error{reset}{color['t-pink']}: {color['magenta']}{e}")
    finally:
        match result:
            case 0:
                result = f"{color['t-green']}Successfully sent email"
            case 1:
                result = f"{color['t-red']}Email not sent"
            case _:
                pass
        clear_line()
        print(f"{notice} {color['t-pink']}{style['underline']}Result{reset}{color['t-pink']}: {result}{reset}")

    time.sleep(2)
    input(f"\n{wait} {color['t-pink']}{style['bold']}Press ENTER to exit")

if __name__ == "__main__":
    cli()