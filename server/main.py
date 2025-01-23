#!/usr/bin/python
import server.server as server
import getopt
import random
import string
import sys
from typing import List


def main(argv):
    # Default
    words = 4
    caps = 0
    nums = 0
    symbols = 0

    try:
        opts, args = getopt.getopt(argv, "hw:c:n:s:")
    except getopt.GetoptError:
        print('For help: ./xkcdpwgen -h')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]')
            sys.exit()
        elif opt in "-w":
            words = int(arg)
        elif opt in "-c":
            caps = int(arg)
        elif opt in "-n":
            nums = int(arg)
        elif opt in "-s":
            symbols = int(arg)
    print(server.pwgen(words, caps, nums, symbols))

if __name__ == "__main__":
    main(sys.argv[1:])
