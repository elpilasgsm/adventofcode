inputData = [val.replace("\n", "") for val in open("input.txt").readlines()]
# inputData = [val.replace("\n", "") for val in open("example.txt").readlines()]

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

pointsAutoComplete = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

brackets = {
    "(": ")",
    "{": "}",
    "<": ">",
    "[": "]",
}


def autocompleteOrder(stack):
    autocomplData = []

    while len(stack) != 0:
        autocomplData.append(brackets[stack.pop()])
    # print(autocomplData)
    return autocomplData


def autocompleteScore(autocomplData):
    sum = 0
    for i in autocomplData:
        sum = 5 * sum + pointsAutoComplete[i]
    # print(sum)
    return sum


errorScore = 0
autocompleteScores = []
for row in inputData:
    corrupted = False
    last = []
    for char in row:
        if char in brackets:
            last.append(char)
            continue
        else:
            lastOpen = last.pop()
            if brackets[lastOpen] != char:
                corrupted = True
                errorPoint = points[char]
                errorScore = errorScore + errorPoint
                # print("Error. expected: {}, found: {}, score: {}, totalScore: {}".format(brackets[lastOpen], char,
                #                                                                   errorPoint, errorScore))
    if corrupted:
        continue

    autocompleteScores.append(autocompleteScore(autocompleteOrder(last)))

print("Part 1: {}".format(errorScore))
print("Part 2: {}".format(sorted(autocompleteScores)[len(autocompleteScores) // 2]))
