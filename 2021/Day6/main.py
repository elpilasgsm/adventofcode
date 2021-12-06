data = open("input.txt").read()
PERIOD = 7


# data = open("example.txt").read()
def oneFishProducing(init, daysLeft):
    return ((daysLeft - init) - (daysLeft - init) % PERIOD) / PERIOD


initData = [int(i) for i in data.split(",")]
print("initData=" + str(initData))
toBeAdded = 0
for day in range(0, 256):
    for fishNum in range(len(initData)):
        if initData[fishNum] == 0:
            toBeAdded = toBeAdded + 1
            initData[fishNum] = 6
        else:
            initData[fishNum] = initData[fishNum] - 1
    if toBeAdded > 0:
        for i in range(toBeAdded):
            initData.append(8)
        toBeAdded = 0
    if day % 20 == 0:
        print("At day: " + str(day) + " len: " + str(len(initData)))
print(len(initData))
