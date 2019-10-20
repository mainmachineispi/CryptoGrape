import sys, random, hashlib
from datetime import datetime # This still makes you type datetime.*, but otherwise i'd be typing datetime.datetime.*
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
    createWallet();
    
print(Fore.GREEN + '[-] Wallet file found.')

def createWallet():
    print(Fore.CYAN + '[-] Generating wallet...')
    wallet_id = hashlib.sha512(str(random.uniform(0,200)) + datetime.now()).hexdigest()
    wallet = open('wallet.cg', 'w')
    wallet.write("CGWallet")
    wallet.write(wallet_id)
    wallet.close()
    print("WALLET ID: " + wallet_id)
    print(Fore.GREEN + "Generation success! Restart CryptoGrape to continue.")
    sys.exit(0)
