import os
print("pinger is currently dead we need to fix it")
hostname = input("server to check: ")
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
    print(hostname + " is up!")
else:
    print(hostname + " is down")
