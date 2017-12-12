# Advent of Code 2017
# Day 2 - Part II
# Python


f = open("advent02.txt", "r")
allLinesList = f.readlines()

sumTotal = 0

for thisLine in allLinesList:
    thisLineArr = thisLine.split("\t")

    for i in range (0, len(thisLineArr)):  # For each number on the line...
        numOne = thisLineArr[i]  # Grab a number.

        for j in range(i + 1, len(thisLineArr)):  # Then check against every other number in the line, after it.
            numTwo = thisLineArr[j]  # Call this numTwo, for convenience.

            if int(numOne) % int(numTwo) == 0:  # Using modulo to see if wholly divisible in one direction.
                #print("LINE ONE: " + str(numOne) + " TWO: " + str(numTwo) + "")
                sumTotal += int(numOne) / int(numTwo)
                break
            elif int(numTwo) % int(numOne) == 0:  # Using modulo to see if wholly divisible in the other direction.
                #print("LINE TWO: " + str(numOne) + " ONE: " + str(numTwo) + "")
                sumTotal += int(numTwo) / int(numOne)
                break

print("TOTAL: " + str(sumTotal))
