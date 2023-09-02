#!/usr/bin/python

import getopt
import random
import string
import sys
from typing import List


def main(argv):
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
    print(pwgen(words, caps, nums, symbols))


def pwgen(words, caps, nums, symbols):
    result = []

    # open the words.txt file
    f = open("words.txt", "r")

    # lowercase words in an array
    for line in f:
        result.append(line.strip("\n").lower())

    rand = random.choices(result, k=words)
    rand.append("")

    while caps > 0:
        # add a check if it is already capitalized
        wordr = random.choice(rand)
        if wordr.lower() == wordr and wordr != "":
            capitalwordr = wordr.capitalize()
            rand.remove(wordr)
            rand.append(capitalwordr)
            caps -= 1

    while nums > 0:
        wordr = random.choice(rand)
        rand.remove(wordr)
        wordr += random.choice(string.digits)
        rand.append(wordr)
        nums -= 1

    while symbols > 0:
        wordr = random.choice(rand)
        rand.remove(wordr)
        wordr += random.choice(string.punctuation)
        rand.append(wordr)
        symbols -= 1
    random.shuffle(rand)
    pw = "".join(rand)
    return pw


if __name__ == "__main__":
    main(sys.argv[1:])
