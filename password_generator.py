import random
import string

#Function for validating GUI input
def validate_pwgen(words, nums, caps, symbols):
    invalid = False

    try:
        nums = int(nums)
        if nums < 0:
            raise Exception("Input cannot be negative")
    except:
        invalid = True
        print("Invalid number input")

    try:
        caps = int(caps)
        if caps < 0:
            raise Exception("Input cannot be negative")
    except:
        invalid = True
        print("Invalid caps input")

    try:
        symbols = int(symbols)
        if symbols < 0:
            raise Exception("Input cannot be negative")
    except:
        invalid = True
        print("Invalid symbols input")

    try:
        words = int(words)
        if words < 0:
            raise Exception("Input cannot be negative")
        if words < nums or words < caps or words < symbols:
            raise Exception("Words must be greater than other inputs")
    except:
        invalid = True
        print("Invalid word input")

    return invalid == False

#Function for generating passcode
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