#!/usr/bin/env python

import os
from colorama import init, Fore
from pyfiglet import Figlet

# Initialize Colorama
init()

os.system("apt-get install figlet")
os.system("clear")

f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('Mac Channger') + Fore.RESET)

# os.system(Fore.BLUE + "figlet Mac Channger" + Fore.RESET)
print(Fore.RED + "          | - | Made By : f3nr1r - Cyber Security | - |         " + Fore.RESET)
    
print("""

1) Mac Address Random
2) Mac Address Manual
3) Mac Address Original

""")

choice = input("Enter Transaction Number: ")

if(choice=="1"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    
    print("\033[92mNew Mac Address Random Created !")
    
elif(choice=="2"):
    macaddress = input("Enter New Mac Address: ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac " + macaddress + " eth0 ")
    os.system("ifconfig eth0 up")
    
    print("\033[92mNew Mac Address Manual Created !")
    
elif(choice=="3"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    
    print("\033[92mNew Mac Address Original Created !")
    
else:
    print("You made a wrong choice, it's restarting...")
    print("python3 mac_channger.py")
