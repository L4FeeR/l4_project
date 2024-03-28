#!/usr/bin/python3
import random, sys, time
from random import randint
from colors import *
am=[]
def ran_gen(SIZE, LIST, SEC):
	print(reset)
	n=[]
	al=[chr(x).lower() for x in range(65, 91)]
	al.extend(al)
	LENGTH=len(al)
	for x in range(0, SIZE):
	    n.extend(random.sample(al,1))
	    sys.stdout.write("\r\t"+white+" Here Your Letter : "+yellow+n[x])
	    time.sleep(SEC)
	return n




def check_gen(LIST):
	print(reset)
	print()
	fd=str(input(purple+"[+]Enter The letters :"+blue+" "))
	print()
	print()
	if fd==''.join(LIST):
	    print(green+"You Pass"+reset) 
	else:
	    print(red+"You Failed")
	print()
	print(white+"Answer Is : "+blink+green+"",''.join(LIST))
	print(reset)


def loading():
	try:
		bar= ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
		bar.extend(bar)
		bar.extend(bar)
		for i in bar:
	                sys.stdout.write("\r"+i)
        	        time.sleep(0.1)
        	        sys.stdout.flush()
	except KeyboardInterrupt:

		print(strike+"\n\t\t\t[+]Skipping Intro"+reset)
		time.sleep(0.8)
