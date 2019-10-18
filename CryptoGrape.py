import sys
from colorama import Fore, Back, Style
print(Fore.CYAN + '[-] CryptoGrape starting...')
print(Fore.GREEN)
print("   _____                  _         _____                      ")
print("  / ____|                | |       / ____|                     ")
print(" | |     _ __ _   _ _ __ | |_ ___ | |  __ _ __ __ _ _ __   ___ ")
print(" | |    | '__| | | | '_ \| __/ _ \| | |_ | '__/ _` | '_ \ / _ \\")
print(" | |____| |  | |_| | |_) | || (_) | |__| | | | (_| | |_) |  __/")
print("  \_____|_|   \__, | .__/ \__\___/ \_____|_|  \__,_| .__/ \___|")
print("               __/ | |                             | |         ")
print("              |___/|_|                             |_|")
print("")
print("V0.1")
print(Style.RESET_ALL)
try:
    wallet = open('wallet.cg', 'rb')
except FileNotFoundError:
    print(Fore.RED + '[!] Wallet file not found.' + Style.RESET_ALL)
    wallet = open('wallet.cg', 'w')
    sys.exit(1)
    
print(Fore.GREEN + '[-] Wallet file found.')