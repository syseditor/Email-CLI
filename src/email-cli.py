# Main file - app runner

import os

from decoration import color, style, reset

# Symbols
plus = f"{style['bold']}{color['dark gray']}[{reset}{color['green']}+{style['bold']}{color['dark gray']}]{reset}"
notice = f"{style['bold']}{color['dark gray']}[{reset}{color['n-blue']}!{style['bold']}{color['dark gray']}]{reset}"
warning = f"{style['bold']}{color['dark gray']}[{reset}{color['w-red']}!{style['bold']}{color['dark gray']}]{reset}"

def cli(): 
    # Cleaning the cli window
    system = os.name
    if system == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
    # Welcome message
    print(f'''
                                {color['red']}Welcome to Email-ClI, a CLI used to email people!
                                        {color['magenta']}Credits: syseditor (GitHub)
    ''')

    #Test block
    print(f"{plus} Wazzup bitch")
    print(f"{notice} Wazzupt bitch")
    print(f"{warning} Wzzzupt bitch")

    input(f'{reset}Press any key to exit')

if __name__ == "__main__":
    cli()