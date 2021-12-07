import re

resp = open("input.txt").readlines()
# resp = open("example.txt").readlines()
regex = r"^(\d*)\-(\d*)\s([a-z])\:\s([a-z]*)$"

validOne = 0
validTwo = 0


def parse(str):
    matches = re.search(regex, str, re.IGNORECASE)
    if matches:
        return int(matches.group(1)), int(matches.group(2)), matches.group(3), matches.group(4)
    else:
        return None


def getNumOfChar(char, str):
    return str.count(char)


def partOne(str):
    valid = 0
    min, max, char, password = parse(i)
    num = getNumOfChar(char, password)
    if num >= min and num <= max:
        valid = 1
    return valid


def partTwo(data):
    min, max, char, password = parse(data)
    occurance = 0
    lenP = len(password)
    if lenP <= min:
        return 0

    if password[min - 1] == char:
        occurance = occurance + 1

    if max > lenP:
        return occurance

    if password[max - 1] == char:
        occurance = occurance + 1

    if occurance == 1:
        print("VALID > Password: {}, min: {}, max: {}, char: {}".format(password, min, max, char))
        return 1
    return 0


for i in resp:
    validOne = validOne + partOne(i)
    validTwo = validTwo + partTwo(i)

print("Part #1: " + str(validOne))
print("Part #2: " + str(validTwo))
