import copy

#inputData = open("example.txt").readlines()
inputData = open("input.txt").readlines()

START = "start"
END = "end"

VERTEXES = {}
COUNTER = 0


def isBig(c):
    return c.isupper()


for row in inputData:
    splitted = row.replace("\n", "").split("-")
    if splitted[0] not in VERTEXES:
        VERTEXES[splitted[0]] = set()
    VERTEXES[splitted[0]].add(splitted[1])
    if splitted[1] not in VERTEXES:
        VERTEXES[splitted[1]] = set()
    VERTEXES[splitted[1]].add(splitted[0])

#print(VERTEXES)


def inList(el, lst):
    return el in lst


def isEnoughSmall(el, lst):
    # if lst["singleCave"] is None and el != START and el != END:
    #     lst["singleCave"] = el

    return (el == lst["singleCave"] and lst['path'].count(el) == 2) or (el != lst["singleCave"] and el in lst['path'])


PATHES = set()

def getPath(startPoint, path):
    path.append(startPoint)
    if startPoint == END:
        PATHES.add(",".join(path))
        return
    if VERTEXES[startPoint]:
        for vert in VERTEXES[startPoint]:
            if not isBig(vert) and inList(vert, path):
                continue
            else:
                getPath(vert, copy.copy(path))


def getPath2(startPoint, path):
    path['path'].append(startPoint)
    if startPoint == END:
        PATHES.add(",".join(path['path']))
        return
    if VERTEXES[startPoint]:
        for vert in VERTEXES[startPoint]:
            if not isBig(vert) and isEnoughSmall(vert, path):
                continue
            else:
                getPath2(vert, {"singleCave": path['singleCave'], "path": copy.copy(path['path'])})


curPoint = START
getPath(curPoint, [])
print("Part #1: {}".format(len(PATHES)))

PATHES = set()
for j in VERTEXES:
    if not isBig(j) and j != START and j != END:
        getPath2(curPoint, {"singleCave": j, "path": []})
print("Part #2: {}".format(len(PATHES)))
