from subprocess import call
import time
import sys


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


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 40)


slowprint(
    f"{bcolors.GREEN}Welcome to REPLUX beta v 0.0.6\ncreated by valhallaboi and puzzle_shock1\n Use help to see command list"
)


def replux():
    while True:
        command = input(f"{bcolors.GREEN}$ ")
        #clear
        if command == "clear":
            call(["python", "replux/clear.py"])
            return replux()

        #ddos
        if command == "sudo ddos":
            call(["python", "replux/ddos.py"])
        #ddos
        if command == "ddos":
            call(["python", "replux/sudoerr.py"])
        #help
        elif command == "help":
            call(["python", "replux/help.py"])
        #ip
        elif command == "ip a":
            call(["python", "replux/ip.py"])  #pinger
        elif command == "ping":
            call(["python", "replux/pinger.py"])
        #star wars
        elif command == "play-sw":
            call(["python", "replux/starwars.py"])
        #url
        elif command == "open-url":
            call(["python", "replux/url.py"])
        #discord-gift
        elif command == "discord-gift":
            call(["python", "replux/giftcode.py"])
        #tt bot
        elif command == "tiktok-bot":
            call(["python", "replux/ttbot.py"])
        #cpu usage check
        elif command == "sudo cpu":
            call(["python", "replux/checkc.py"])
        #ram usage check
        elif command == "sudo ram":
            call(["python", "replux/checkr.py"])
        #disk usage check
        elif command == "sudo disk":
            call(["python", "replux/checkd.py"])
        #diskerr
        elif command == "disk":
            call(["python", "replux/sudoerr.py"])
        #ramerr
        elif command == "ram":
            call(["python", "replux/sudoerr.py"])
        #cpu err
        elif command == "cpu":
            call(["python", "replux/sudoerr.py"])
        #school project
        elif command == "school":
            call(["python", "replux/schoolStuff/school.py"])
        #about
        elif command == "about":
            call(["python", "replux/about.py"])  
        #tiktok gen
        elif command == "accgen":
            call(["python", "replux/ttbot.py"])
        #rps
        elif command == "rps":
            call(["python", "replux/rps.py"])
        #tictactoe
        elif command == "tctctoe":
          call(["python", "replux/tictactoe.py"])
        #just an enter
        elif command == "":
            replux()
        #when wrong
        else:
            print("no command called " + command +
                  "'\nUse help to show command list")


replux()
