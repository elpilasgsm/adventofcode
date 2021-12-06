#
from collections import Counter

#data = open("example.txt").read()
data = open("input.txt").read()
PERIOD = 7

cache = {}

def buildKey(init,days):
    return str(init) + "X" + str(days)
# data = open("example.txt").read()
def oneFishProducing(init, daysLeft):
    key = buildKey(init,daysLeft)
    if init > daysLeft:
        cache[key] = 0
        return 0
    dif = daysLeft - init
    newFishes = 0
    while newFishes * PERIOD < dif:
        newFishes = newFishes + 1

    sum = 0
    for i in range(newFishes):
        localKey = buildKey(9 + (init + (PERIOD * i)), daysLeft)
        if localKey in cache:
            sum = sum + cache[localKey]
        else:
            sum = sum + oneFishProducing(9 + (init + (PERIOD * i)), daysLeft)
    cache[key] = newFishes + sum
    return newFishes + sum

#1710623015163
initData = [int(i) for i in data.split(",")]
toBeAdded = 0
days = 256
val = len(initData)
counter = Counter(initData)
#
for fish in counter:
    val = val + oneFishProducing(fish, days) * counter[fish]

print(val)
