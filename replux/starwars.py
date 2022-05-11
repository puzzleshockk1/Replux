import time
from telnetlib import Telnet

print("the animation is not by REPLUX")
time.sleep(5)
with Telnet('towel.blinkenlights.nl') as tn:
    tn.interact()