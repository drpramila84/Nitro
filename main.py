import requests
import random
import string
import base64
import os
import time
import winsound 
from colorama import init
from pystyle import Colors, Colorate, Center
import shutil


init()                                                                                                                                                                                                                                                                                                                                                                                                          # made by sudero https://discord.gg/rBbC8rBwvy                                                                                          
os.system('title Sudero Gen ^| Discord.gg/rBbC8rBwvy ^| Nitro Gen ^| Version : 2.1')
os.system("mode con: cols=100 lines=30")

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

# --- Core Functions ---
def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def check_nitro_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return None
    
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return None

def get_image_base64(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode('utf-8')
    except:
        pass
    return None

def update_webhook(webhook_url):
    image_url = "https://cdn.discordapp.com/attachments/1250078637215060068/1262709684939259944/Red_and.png"
    image_base64 = get_image_base64(image_url)

    if image_base64:
        data = {"name": "Sudero", "avatar": f"data:image/png;base64,{image_base64}"}
        response = requests.patch(webhook_url, json=data)
        if response.status_code == 200:
            print(f"{g}[{t}] Webhook updated successfully{rs}")
        else:
            print(f"{r}[{t}] Webhook update error: {response.status_code}{rs}")

def send_to_webhook(webhook_url, code, status):
    full_code_url = f"https://discord.gift/{code}"
    data = {
        "content": f"Generated Code: {full_code_url} >> {'✅ Valid' if status else '❌ Invalid'}"
    }
    requests.post(webhook_url, json=data)

def save_good_code(code):
    with open("Sudero generated.txt", "a") as f:
        f.write(f"https://discord.gift/{code}\n")
    # Makes a sound when a valid code is found!
    winsound.Beep(1000, 500)  # 1000Hz, 0.5 sec duration time of the beeeeeeep sound 



def print_banner():
    banner = r"""
       
            _   ___ __                ______              _    _____ 
           / | / (_) /__________     / ____/__  ____     | |  / /__ \
          /  |/ / / __/ ___/ __ \   / / __/ _ \/ __ \    | | / /__/ /
         / /|  / / /_/ /  / /_/ /  / /_/ /  __/ / / /    | |/ // __/ 
        /_/ |_/_/\__/_/   \____/   \____/\___/_/ /_/     |___//____/ 
                                                             
"""
    BLUE = '\033[38;2;50;100;255m'
    RESET = '\033[0m'
    print(f"{BLUE}{banner}{RESET}")


def main():
    while True:
        print_banner()
        webhook_url = input(f" {t} {d}[{rs}${d}]{rs} WebHook >> ")


        send_invalid_choice = input(f" {t} {d}[{rs}${d}]{rs} Send invalid Nitro URLs to webhook? (y/n) >> ").lower()
        send_invalid = send_invalid_choice.startswith("y")

        num_codes = int(input(f" {t} {d}[{rs}${d}]{rs} How Many Nitro Codes >> "))

        update_webhook(webhook_url)

        for _ in range(num_codes):
            code = generate_nitro_code()
            status = check_nitro_code(code)

            if status is True or (status is False and send_invalid):
                send_to_webhook(webhook_url, code, status)

            if status is True:
                print(f"{g}[{t}] VALID >> https://discord.gift/{code}{rs}")
                save_good_code(code)
            elif status is False:
                print(f"{r}[{t}] INVALID >> https://discord.gift/{code}{rs}")
            else:
                print(f"{d}[{t}] UNKNOWN/ERROR >> {code}{rs}")

        input(f" {t} {d}[{rs}${d}]{rs} The generator stopped. Press Enter to retry...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                             # made by sudero https://discord.gg/rBbC8rBwvy
    main()
