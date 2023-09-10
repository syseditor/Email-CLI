# Main file - app runner

import os
import sys
import time
import smtpd
# import getpass

from decoration import *
from methods import *

# Symbols
plus = f"{style['bold']}{color['dark gray']}[{reset}{color['green']}+{style['bold']}{color['dark gray']}]{reset}"
notice = f"{style['bold']}{color['dark gray']}[{reset}{color['n-blue']}!{style['bold']}{color['dark gray']}]{reset}"
warning = f"{style['bold']}{color['dark gray']}[{reset}{color['w-red']}!{style['bold']}{color['dark gray']}]{reset}"

def cli():
    system = os.name
    # Creating the SMTP server
    # os.system('python -m smtpd -n localhost:1025') # Debugging server
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
    # Email
    sender = input(f"{plus} {color['t-yellow']}Enter your email address: {color['a-green']}")
    cursor('up', 1)
    clear_line()
    # Password
    password = input(f"{plus} {color['t-yellow']}Enter your email's password: {color['a-green']}")
    cursor('up', 1)
    clear_line()
    login("test@gmail.com", password)
    time.sleep(2)
    input(f'{reset}Press any key to exit')

if __name__ == "__main__":
    cli()