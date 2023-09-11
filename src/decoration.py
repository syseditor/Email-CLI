# Contains constants and functions for various text decoration styles

reset = '\033[0;0m' # Resets all decorations

color = { # Text colors
    'red' : '\033[38;5;196m',
    'magenta' : '\033[38;5;201m',
    'dark gray' : '\033[38;5;240m', # 240 or 241
    'green' : '\033[38;5;46m', # 46 or 2
    'n-blue' : '\033[38;5;39m',
    'w-red' : '\033[38;5;160m',
    't-pink' : '\033[38;5;224m', # 15 or 224
    't-yellow' : '\033[38;5;226m',
    't-green' : '\033[38;5;35m', # 35 or 34
    't-red' : '\033[38;5;1m',
    'a-green' : '\033[38;5;10m',
    'wt-purple' : '\033[38;5;93m'
}

style = { # Text styles
    'bold' : '\033[1m',
    'underline' : '\033[4m'
}

# Symbols
plus = f"{style['bold']}{color['dark gray']}[{reset}{color['green']}+{style['bold']}{color['dark gray']}]{reset}"
notice = f"{style['bold']}{color['dark gray']}[{reset}{color['n-blue']}!{style['bold']}{color['dark gray']}]{reset}"
warning = f"{style['bold']}{color['dark gray']}[{reset}{color['w-red']}!{style['bold']}{color['dark gray']}]{reset}"
wait = f"{style['bold']}{color['dark gray']}[{reset}{color['wt-purple']}...{style['bold']}{color['dark gray']}]{reset}"

def cursor(move: str, lines: int): # Cursor navigation
    if lines > 0:
        match move:
            case 'up':
                return print(f'\033[{lines}A', end = '\r', flush = True)
            case 'down':
                return print(f'\033[{lines}B', end = '\r', flush = True)
            case 'right':
                return print(f'\033[{lines}C', end = '', flush = True)
            case 'left':
                return print(f'\033[{lines}D', end = '', flush = True)
            case _:
                raise Exception('Invalid move')
    else:
        raise TypeError('Lines argument must be above 0')

def clear_line(): # Clears current line
    return print('\x1b[2K', end = '\r')