import requests
import sys
from colorama import Fore, init
from time import sleep
import random

init(autoreset=True)

CONTACTS = 'Telegram: @ItsReZNuM | Instagram: ReZ.NuM | GitHub: https://github.com/ItsReZNuM'

def unscramble_effect(text, delay=0.05):
    """Display text with an unscramble effect."""
    chars = list(text)
    displayed = [' ' for _ in chars]
    indices = list(range(len(chars)))
    random.shuffle(indices)
    
    for i in indices:
        displayed[i] = chars[i]
        sys.stdout.write('\r' + Fore.LIGHTGREEN_EX + ''.join(displayed))
        sys.stdout.flush()
        sleep(delay)
    print()

print(f"""{Fore.CYAN}


$$$$$$$\            $$$$$$$$\ $$\   $$\           $$\      $$\ 
$$  __$$\           \____$$  |$$$\  $$ |          $$$\    $$$ |
$$ |  $$ | $$$$$$\      $$  / $$$$\ $$ |$$\   $$\ $$$$\  $$$$ |
$$$$$$$  |$$  __$$\    $$  /  $$ $$\$$ |$$ |  $$ |$$\$$\$$ $$ |
$$  __$$< $$$$$$$$ |  $$  /   $$ \$$$$ |$$ |  $$ |$$ \$$$  $$ |
$$ |  $$ |$$   ____| $$  /    $$ |\$$$ |$$ |  $$ |$$ |\$  /$$ |
$$ |  $$ |\$$$$$$$\ $$$$$$$$\ $$ | \$$ |\$$$$$$  |$$ | \_/ $$ |
\__|  \__| \_______|\________|\__|  \__| \______/ \__|     \__|
                                                                                                            
                                                               
                                                                   
                                                                      
                                                                      
    {Fore.YELLOW}ReZNuM's Tool to Delete Telegram Account 
""")
unscramble_effect(CONTACTS)

def confirm_deletion():
    """Get initial confirmation from user."""
    confirm = input(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.YELLOW}Are you sure you want to delete your Telegram account? This action is irreversible! (yes/no): {Fore.RED}").strip().lower()
    if confirm != 'yes':
        print(f"{Fore.GREEN}Operation cancelled.")
        sys.exit()
    final_confirm = input(f"{Fore.RED}[{Fore.YELLOW}!!{Fore.RED}] {Fore.YELLOW}Are you ABSOLUTELY sure you want to delete your account? This is your final confirmation! (yes/no): {Fore.RED}").strip().lower()
    if final_confirm != 'yes':
        print(f"{Fore.GREEN}Operation cancelled.")
        sys.exit()
    return True

def send_code(phone):
    with requests.Session() as req:
        try:
            res = req.post("https://my.telegram.org/auth/send_password", data={"phone": phone})
            if 'random_hash' in res.text:
                return res.json()['random_hash'], req
            elif "too many tries" in res.text:
                print(f"{Fore.RED}Your account has been banned! Please try again in 8 hours")
                sys.exit()
            else:
                print(f"{Fore.RED}Unknown error occurred. Please try again later.")
                sys.exit()
        except Exception as e:
            print(f"{Fore.RED}Server error: {e}")
            sys.exit()

def check_code(phone, random_hash, code, session):
    try:
        res = session.post("https://my.telegram.org/auth/login", data={
            "phone": phone,
            "random_hash": random_hash,
            "password": code
        })
        if res.text == "true":
            return session
        elif "too many tries" in res.text:
            print(f"{Fore.RED}Too many tries. Please try again later.")
            sys.exit()
        elif "Invalid confirmation code!" in res.text:
            print(f"{Fore.RED}Invalid code. Please try again.")
            sys.exit()
        else:
            print(f"{Fore.RED}Unknown error: {res.text}")
            sys.exit()
    except Exception as e:
        print(f"{Fore.RED}Server error: {e}")
        sys.exit()

def delete_account(session):
    try:
        req = session.get("https://my.telegram.org/delete")
        if "Delete Your Account" in req.text:
            hash_value = req.text.split("hash: '")[1].split("'")[0]
            res = session.post("https://my.telegram.org/delete/do_delete", 
                             data={"hash": hash_value, "message": "goodbye"})
            if res.text == "true":
                return True
            else:
                print(f"{Fore.RED}Failed to delete account: {res.text}")
                sys.exit()
        else:
            print(f"{Fore.RED}Could not access delete page.")
            sys.exit()
    except Exception as e:
        print(f"{Fore.RED}Server error: {e}")
        sys.exit()

phone = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter your number with country code [Ex: +98XXXXXX]: {Fore.RED}")
if confirm_deletion():
    random_hash, session = send_code(phone)
    code = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter the code sent to your Telegram account: {Fore.RED}")
    session = check_code(phone, random_hash, code, session)
    if delete_account(session):
        sleep(3)
        print(f"""{Fore.GREEN}

$$$$$$$\   $$$$$$\   $$$$$$\  $$\      $$\ $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |$$ |
$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\  $$$$ |$$ |
$$$$$$$\ |$$ |  $$ |$$ |  $$ |$$\$$\$$ $$ |$$ |
$$  __$$\ $$ |  $$ |$$ |  $$ |$$ \$$$  $$ |\__|
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |    
$$$$$$$  | $$$$$$  | $$$$$$  |$$ | \_/ $$ |$$\ 
\_______/  \______/  \______/ \__|     \__|\__|
                                               
                                               
                                               

    {Fore.CYAN}Account successfully deleted!
""")