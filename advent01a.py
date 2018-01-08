# Advent of Code 2017
# Day 1 - Part I
# Python


f = open("advent01.in", "r")
allFileStr = f.read()

sumTotal = 0  # To keep track of total.
iter = 0  # To keep track of iterator.
for thisChar in allFileStr:  # Probably could have used a standard for loop, since I'm using an iterator, but whatever.
    nextChar = allFileStr[(iter + 1) % len(allFileStr)]  # Using the modulo to wrap the value back to the beginning.
    if thisChar == nextChar:
        sumTotal += int(thisChar)
    iter += 1


print("TOTAL: " + sumTotal)
