def calcGammaAndEpsilon(resp):
    strLen = len(resp[0]) - 1
    gRate = [0] * strLen
    eRate = [0] * strLen
    for r in resp:
        for c in range(strLen):
            inc = 1
            if int(r[c]) < 1:
                inc = -1 * inc
            gRate[c] = gRate[c] + inc

    for i in range(strLen):
        if gRate[i] >= 0:
            gRate[i] = '1'
            eRate[i] = '0'
        else:
            gRate[i] = '0'
            eRate[i] = '1'
    return {"gammaRate": gRate, "epsilonRate": eRate}


def filterData(retVal, mask, curPos, max):
    if len(retVal) == 1:
        return retVal

    retVal = [value for value in retVal if value[curPos] == mask[curPos]]
    data = calcGammaAndEpsilon(retVal)
    if max == True:
        data = data["gammaRate"]
    else:
        data = data["epsilonRate"]
    return filterData(retVal, data, curPos + 1, max)


resp = open("input.txt").readlines()
data = calcGammaAndEpsilon(resp)
gammaRate = data["gammaRate"]
epsilonRate = data["epsilonRate"]

print("Part #1: "+ str(int(''.join(gammaRate), 2) * int(''.join(epsilonRate), 2)))
oxy = filterData(resp, gammaRate, 0, True)
co2 = filterData(resp, epsilonRate,0, False)

print("Part #2: " + str(int(oxy[0], 2) * int(co2[0], 2)))
#Part #1: 3985686
#Part #2: 2555739