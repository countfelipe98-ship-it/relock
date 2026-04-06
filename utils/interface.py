import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

RED = "\033[38;5;196m"
WHITE = "\033[38;5;255m"
RESET = Style.RESET_ALL

# Nome SANCTUARY em Bloco Sólido (Estilo das fotos, mas seguro para mobile)
SANCTUARY_ART = r"""
████  ███  █  █  ███ ████ █  █  ███  ██  █  █
█    █   █ ██ █ █     █   █  █ █   █ █ █ █  █
 ██  █████ █ ██ █     █   ████ █████ ██  ████
   █ █   █ █  █ █     █   █  █ █   █ █ █   █ 
████ █   █ █  █  ███  █   █  █ █   █ █  █  █ 
"""

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_gradient_ascii():
    clear_screen()
    try:
        width = os.get_terminal_size().columns
    except:
        width = 80

    lines = SANCTUARY_ART.strip('\n').split('\n')
    
    for line in lines:
        # Efeito Metade Vermelho / Metade Branco
        mid = len(line) // 2
        left_part = line[:mid]
        right_part = line[mid:]
        
        # Colado na esquerda para não vazar nunca
        print(f"{RED}{left_part}{WHITE}{right_part}{RESET}")

    # Linha de separação que se ajusta à tela
    line_sep = "─" * (width - 1)
    print(f"{RED}{line_sep}{RESET}")
    print(f"{RED} AUTHOR: {WHITE}xysix {RED}| VERSION: {WHITE}1.0 {RED}| STATUS: {WHITE}ONLINE{RESET}")
    print(f"{RED}{line_sep}{RESET}")

def wait_enter():
    print(f"\n{RED} Pressione Enter para continuar...{RESET}")
    sys.stdin.readline()

