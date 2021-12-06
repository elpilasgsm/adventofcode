from copy import copy

import numpy


def toCards(data):
    cards = []
    card = []
    offset = 2
    for rowNum in range(offset, len(data)):
        if rowNum > 3 and (rowNum - 1) % 6 == 0:
            cards.append(numpy.array(copy(card)))
            card = []
            continue
        card.append([int(i) for i in data[rowNum].split(" ") if i])
    cards.append(numpy.array(copy(card)))
    return cards


def findData(card, num):
    for rowNum in range(len(card)):
        for cellNum in range(len(card[rowNum])):
            if card[rowNum][cellNum] == num:
                card[rowNum][cellNum] = 0


def checkData(card):
    if 0 in card.sum(axis=0) or 0 in card.sum(axis=1):
        return card.sum()
    return None


resp = open("input.txt").readlines()
# resp = open("example.txt").readlines()

myCards = toCards(resp)
print("len:" + str(len(myCards)))

numbers = [int(i) for i in resp[0].split(",")]
print("Numbers: " + str(numbers))
cardWon = []
firstCardFound = False
for i in numbers:
    for cardNum in range(len(myCards)):
        card = myCards[cardNum]
        findData(card, i)
        retVal = checkData(card)
        if retVal is not None:
            if not firstCardFound :
                print("1st Card Won at number:" + str(i) + ". Answer is: " + str(retVal * i))
                firstCardFound = True
            if len(myCards) == 1:
                print("Last Card Won at number:" + str(i) + ". Answer is: " + str(retVal * i))

            cardWon.append(cardNum)

    if len(cardWon) > 0:
        temp = []
        for i in range(len(myCards)):
            if i not in cardWon:
                temp.append(myCards[i])
        cardWon = []
        myCards = temp

# Part 2
# print("Cards:" + str(myCards))
