#!/usr/bin/python3

import module, os, sys, time, colors
from module import *
#RN=ran_gen(d, am)
#print(RN)
#check_gen(RN)
loading()
def run(SEC,MODE):
    d=int(input("/r[+]How Many Letters : "))
    RN=ran_gen(d, am, SEC)
    check_gen(RN)
def menu(DELAY):
    os.system("clear")
    print("\n\n")
    print(underline+"     Menu:",reset)
    print(italic)
    print("     1.["+blue+"E"+reset+italic+"]asy")
    print("     2.["+cyan+"N"+reset+italic+"]ormal")
    print("     3.["+green+"H"+reset+italic+"]ard")
    print("     4.["+red+"G"+reset+italic+"]od Mod")
    print("     0.["+yellow+"E"+reset+italic+"]xit")
    print("\n\n")
    mod=int(input("[+]Enter Game Mod : "))
    if mod==1:
        run(0.8,1)
    elif mod==2:
        run(0.5,2)
    elif mod==3:
        run(0.3,3)
    elif mod==4:
        run(0.1,4)
    elif mod==0:
        exit(0)
    elif mod==99:
        os.system("kill $(pidof nano);nano main.py")
    else:
        print("[-]Invalid Argument! Assuming Normal Mode")
        run(0.8)
    print("\n\n\n")
    time.sleep(DELAY)
while True:
	print()
	menu(2)




