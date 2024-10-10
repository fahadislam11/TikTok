# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: <x>
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2023-06-19 17:44:36 UTC (1687196676)

import os
import sys
import itertools
import threading
import time
import signal
from colorama import Fore, Style
os.system('clear')

COLOR_DEFAULT = Style.RESET_ALL
COLOR_BLUE = Fore.BLUE
COLOR_MAGENTA = Fore.MAGENTA
COLOR_CYAN = Fore.CYAN
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
ICON = '➤ '
ARRAY_ANIMATION = [f'{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}  ', f'   {COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON} ', f'    {COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_RED}{ICON}{COLOR_YELLOW}{ICON}{COLOR_MAGENTA}{ICON}']

class Spinner:

    def __init__(self, message):
        self.message = message
        self.stop_running = False
        self.thread = None
        self.animation_cycle = itertools.cycle(ARRAY_ANIMATION)
        self.columns = shutil.get_terminal_size().columns

    def start(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()

    def _animate(self):
        while not self.stop_running:
            sys.stdout.write(f'\r{self.message} {next(self.animation_cycle)}')
            sys.stdout.flush()
            time.sleep(0.1)

    def stop(self, exit_status):
        self.stop_running = True
        if self.thread is not None:
            self.thread.join()
        sys.stdout.write('\r' + ' ' * self.columns + '\r')
        sys.stdout.flush()
if __name__ == '__main__':
    import shutil
    Spinner = Spinner('\tThis Tools Hasbeen Loading')
    Spinner.start()
    time.sleep(5)
    Spinner.stop(0)
import os
import time
import requests
import random
g = '\x1b[1;32m'
try:
    import getuseragent
except ModuleNotFoundError:
    os.system('pip install getuseragent')
    os.system('clear')
    import getuseragent
from getuseragent import UserAgent
from rich.panel import Panel

def wait():
    for i in range(100):
        print(f'\n\n{g}[ + ] Wait 2 Menite For Next Submit : {i + 1}/120', end='\r')
        time.sleep(1)
        os.system('clear')
r = '\x1b[1;31m'
b = '\x1b[1;34m'
bl = '\x1b[1;30m'
c = '\x1b[1;36m'
p = '\x1b[1;35m'
r = '\x1b[1;31m'
y = '\x1b[1;33m'
w = '\x1b[1;37m'
random_colour = [b, c, g]
ran = random.choice(random_colour)
logo = """\x1b[1;93m(               )       (      
 \x1b[1;93m)\ )   (     ( /(  (    )\ )   
\x1b[1;93m(()/(   )\    )\()) )\  (()/(   
\x1b[1;93m /(_)|(((_)( ((_)((((_)( /(_))  
\x1b[1;93m(_))_|)\ _ )\ _((_)\ _ )(_))_   
\x1b[1;93m| |_  (_)_\(_) || (_)_\(_)   \  
\x1b[1;93m| __|  / _ \ | __ |/ _ \ | |) | 
\x1b[1;93m|_|   /_/ \_\|_||_/_/ \_\|___/
\x1b[1;96m========================================
\x1b[1;91m[TOOLS     =    fahadislam11_ > GIFT]
\x1b[1;92m[MAKING    =    fahadislam ERROR OFC]
\x1b[1;93m[CODING    =    FAHAD SAJU]
\x1b[1;94m[THIS TOOL DECODE + FIX BY ERROR x SAJU ]
\x1b[1;97m========================================"""

def linex():
    print(f'{ran}-----------------------------------{w}')

class TikTokBooster:

    def __init__(self):
        self.ua = UserAgent('ios').Random()
        self.base_url = 'https://api.likesjet.com/freeboost/3'

    def boost_video(self, user: str, link: str) -> dict:
        email = f'suyibislam{random.randint(10000, 99999)}@gmail.com'
        headers = {'Host': 'api.likesjet.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': self.ua}
        data = {'link': link, 'tiktok_username': user, 'email': email}
        response = requests.post(self.base_url, json=data, headers=headers).json()
        return response

def main():
    print(logo)
    print(f'{y} [√]ENTER YOUR TIKTOK USERNAME HERE 👇👇{w}')
    linex()
    print(f'{y} [√]EXAMPLE >>👉 @fahadislam6946👈{w}')
    linex()
    user = input(f' {ran}[?]TikTok UserName:{w} ')
    linex()
    link = input(f' {ran}[?]Video Link: {w}')
    booster = TikTokBooster()
    response = booster.boost_video(user, link)
    if response.get('status'):
        status = f'{g}[√] Successfully 1000 View send{w}'
        print(f'{g}[√] Successfully 1000 View send{w}')
        wait()
        main()
    else:
        status = f"{r}[\u200c#] SORRY I CAN'T SEND VIEW IN YOUR VIDEO{w}"
        print(f"{r}[\u200c#] SORRY I CAN'T SEND VIEW IN YOUR VIDEO{w}")
        wait()
        main()
if __name__ == '__main__':
    main()