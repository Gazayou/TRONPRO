
import random
import time
import requests
from colorama import Fore , Style, ansi

print('Start')
with open("trxAdd.txt","r") as file:
    line_count = 0
    for line in file:
        line != "\n"
        line_count += 1

print("Total Address Loaded This File Import  "+Fore.YELLOW+str(line_count)+Style.RESET_ALL)
mylist = []

with open('trxAdd.txt', newline='',encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

        print(Fore.RED,'Save in the file name "Winner.TXT" can you check this file root folder')
        time.sleep(1)
        print(Fore.GREEN,'Now i run procces check your file and countine work')
        print(Fore.CYAN,'==================== M M D R Z A . C O M ====================',Style.RESET_ALL)
        time.sleep(1)

        continue
