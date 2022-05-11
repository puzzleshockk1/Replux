import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint("REPLUX v 0.0.6\ncreated by valhallaboi and puzzle_shock1")
slowprint("-------------------------------------")
slowprint("What is Replux?")
slowprint("Replux is a opensource terminal made with python")
slowprint("If you need help use help command to see command list")
slowprint("Need special help? Join our discord help server: https://discord.gg/mJrxwaADza")