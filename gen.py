import random
import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print('\033[31m' + """
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
░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░░░░░░░╚═╝░░░""")

print('\033[31m' + """

█▀▀ █▀█ █░░ █░░ █▀█ █░█░█   █▀▄▀█ █▄█   ▄▀█ █░░ ▀█▀   ▀▄▀ █▀▀ █▄▀ █▀▀ █▀▄
█▀░ █▄█ █▄▄ █▄▄ █▄█ ▀▄▀▄▀   █░▀░█ ░█░   █▀█ █▄▄ ░█░   █░█ █▄▄ █░█ ██▄ █▄▀""")

print('\033[31m' + "(e.g if you want 100 put 101)")

much = int(input("how much unchecked tiktok names do you want: "))




chars = "1234567890abcdefghijklmnopqrstuvwxyz"
char =  "123456789abcdefghijklmnopqrstuvwxyz"
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
    endof = ''.join((random.choice(chars) for i in range(1)))
    midleof = ''.join((random.choice(char) for i in range(2)))
    startof = ''.join((random.choice(cha) for i in range(1)))
  
    result = startof + midleof + endof
  

    output = open("unchecked generated names.txt", "a")
    output.write(result + "\n")
print ( str.strip('-') )

print("""

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
""")

print("""

█ █▀▀   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀▀ █░█ █▀▀ █▀▀ █▄▀   ▀█▀ █░█ █▀▀ █▀▄▀█   █▀▀ █▀█   ▀█▀ █▀█
█ █▀░   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▄▄ █▀█ ██▄ █▄▄ █░█   ░█░ █▀█ ██▄ █░▀░█   █▄█ █▄█   ░█░ █▄█ https://github.com/NightfallGT/TikTok-Username-Checker
""")
