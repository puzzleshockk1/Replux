import psutil, os

print("The usage statistics of " + os.getcwd() + " is:")
print(psutil.disk_usage(os.getcwd()))