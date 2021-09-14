import random
import colorama
import os
import sys,time,os
from tkinter import *
from os import system
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

clear = lambda: os.system("cls")

if __name__ == '__main__':
    system('cls && title follow tooxpooxhoox and xcked')

nameof = '\033[31m' + """
░░██╗██╗██╗░░░░░
░██╔╝██║██║░░░░░
██╔╝░██║██║░░░░░
███████║██║░░░░░
╚════██║███████╗
░░░░░╚═╝╚══════╝

░██████╗░███████╗███╗░░██╗░░░██████╗░██╗░░░██╗
██╔════╝░██╔════╝████╗░██║░░░██╔══██╗╚██╗░██╔╝
██║░░██╗░█████╗░░██╔██╗██║░░░██████╔╝░╚████╔╝░
██║░░╚██╗██╔══╝░░██║╚████║░░░██╔═══╝░░░╚██╔╝░░
╚██████╔╝███████╗██║░╚███║██╗██║░░░░░░░░██║░░░
░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░░░░░░░╚═╝░░░"""

nameof2 = '\033[31m' + """

█▀▀ █▀█ █░░ █░░ █▀█ █░█░█   █▀▄▀█ █▄█   ▄▀█ █░░ ▀█▀   ▀▄▀ █▀▀ █▄▀ █▀▀ █▀▄
█▀░ █▄█ █▄▄ █▄▄ █▄█ ▀▄▀▄▀   █░▀░█ ░█░   █▀█ █▄▄ ░█░   █░█ █▄▄ █░█ ██▄ █▄▀"""

for char in nameof:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.000000001)

for char in nameof2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.000000001)
    

print('\033[31m' + "(e.g if you want 100 put 101)")

much = int(input("how much unchecked tiktok names do you want: "))

chars = "1234567890abcdefghijklmnopqrstuvwxyz"
charss =  "123456789abcdefghijklmnopqrstuvwxyz"
cha = "123456789abcdefghijklmnopqrstuvwxyz"
ch = "1234567890abcdefghijklmnopqrstuvwxyz_"
c =  "123456789abcdefghijklmnopqrstuvwxyz_."
k = "123456789abcdefghijklmnopqrstuvwxyz_."





lettersonly = input("do you want characters or characters and underscore and fullstops (y/n)" )
if lettersonly.lower() == 'y':

  for i in range(much):
    endof = ''.join((random.choice(ch) for i in range(1)))
    midleof = ''.join((random.choice(c) for i in range(2)))
    startof = ''.join((random.choice(k) for i in range(1)))
  
    result = startof + midleof + endof
  

    output = open("unchecked generated names.txt", "a")
    output.write(result + "\n")

else:
  for i in range(much):
    end = ''.join((random.choice(chars) for i in range(1)))
    midle = ''.join((random.choice(charss) for i in range(2)))
    start = ''.join((random.choice(cha) for i in range(1)))
  
    result = start + midle + end
  

    output = open("unchecked generated names.txt", "a")
    output.write(result + "\n")
print ( str.strip('-') )

for made in range (much):
    print('\033[31m' + "just created one (for example " + result + ")")
    print('\033[34m' + "just created one (for example " + result + ")")

os.system('cls')
time.sleep(2)

check = """
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗  ██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝  ██║░░░██║████╗░██║██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░  ██║░░░██║██╔██╗██║██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██║░░██║
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░  ██║░░░██║██║╚████║██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██║░░██║
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗  ╚██████╔╝██║░╚███║╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗███████╗██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░█████╗░░██║░░██║
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██╔══╝░░██║░░██║
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░

███╗░░██╗░█████╗░███╗░░░███╗███████╗░██████╗░░░████████╗██╗░░██╗████████╗
████╗░██║██╔══██╗████╗░████║██╔════╝██╔════╝░░░╚══██╔══╝╚██╗██╔╝╚══██╔══╝
██╔██╗██║███████║██╔████╔██║█████╗░░╚█████╗░░░░░░░██║░░░░╚███╔╝░░░░██║░░░
██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗░░░░░░██║░░░░██╔██╗░░░░██║░░░
██║░╚███║██║░░██║██║░╚═╝░██║███████╗██████╔╝██╗░░░██║░░░██╔╝╚██╗░░░██║░░░
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░
"""

for char in check:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0000000001)

print("""

█ █▀▀   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀▀ █░█ █▀▀ █▀▀ █▄▀   ▀█▀ █░█ █▀▀ █▀▄▀█   █▀▀ █▀█   ▀█▀ █▀█
█ █▀░   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▄▄ █▀█ ██▄ █▄▄ █░█   ░█░ █▀█ ██▄ █░▀░█   █▄█ █▄█   ░█░ █▄█ https://github.com/NightfallGT/TikTok-Username-Checker
""")
