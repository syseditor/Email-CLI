import os

from color import color

def cli(): 
    # Cleaning the cli window
    system = os.name
    if system == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
    print(f'''
                                {color['red']}Welcome to Email-ClI, a CLI used to email people!
                                        {color['magenta']}Credits: syseditor (GitHub)
''')
    input(f'{color["reset"]}Press any key to exit')

if __name__ == "__main__":
    cli()