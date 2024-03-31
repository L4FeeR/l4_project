#!/ust/bin/python3
from colors import *
import os, sys, time, requests
os.system("clear")


#BANNER

print(underline+blink+"\t\t\t********************")
print(blue+"\t\t\tPy-Telegram Sender")
print(green+"\t\t\t\t\tv1.1"+reset)
print(reset+underline+blink+"\t\t\t********************\n\n\n\n\n\n"+reset)
#t
t=purple+"["+green+"+"+purple+"]"+reset
t2=green+"["+red+"-"+green+"]"+reset
t3=purple+"["+green+"+"+purple+"]"+reset


#CONFIG
TOKEN="7142033592:AAFy8APbSls_2XhjsLXtvvzm5A54TGV9jx4"
CHAT_ID=-1002043389909
msg=[]
INTERVAL=0.5

NOTES=yellow+"""	To send a multiple line program,
	u need to add %0A to the text , where it need to line break
	otherwise \\n will not work.

	These messages are currently sent to \"@l4testsubject\" telegram group.
"""+reset





#Message Logic
try:
	print(NOTES)
	while True:
		m=input(f"\n\t{t}Enter message to send [CTRL^D,C to end] : ")
		msg.append(m)
		print(msg)
except KeyboardInterrupt:
	print(yellow+"\n\n\t["+green+"CTRL^C"+yellow+"]"+reset+"Message gathering done.")

except EOFError:
	print(yellow+"\n\n\t["+green+"CTRL^D"+yellow+"]"+reset+"Message gathering done.")





num=0
#Message Send Logic Request
os.system("clear")

print("\n\n\t======================")
print("\t    Sending Messages")
print("\t======================")
try:
	for i in msg:
		if msg[num]=="":
        		print(f"\n\t\t{t2}"+red+"No message"+reset+" is sent as there is no message!")
		else:
			url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={i}"
#print(requests.get(url).json())
			requests.get(url).json()
			print(f"\n\t\t{t}Sent : {i}")
			time.sleep(INTERVAL)
		num+=1
except OSError:
	print(f"{t2}"+cyan+"Nerwork not reaching telegram, try connect network again or the ip is blocked!")
