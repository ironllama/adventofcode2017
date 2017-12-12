# Advent of Code 2017
# Day 2 - Part I
# Python


f = open("advent02.txt", "r")
allLinesList = f.readlines()

sumTotal = 0

for thisLine in allLinesList:
    highest = -1  # Just using -1 as a placeholder for "no value", though I probably could have used "". Maybe next time.
    lowest = -1  # Just using -1 as a placeholder for "no value", though I probably could have used "". Maybe next time.

    thisLineArr = thisLine.split("\t")

    for thisNum in thisLineArr:  # Check each number on this line.
        if int(thisNum) > highest: highest = int(thisNum)
        elif int(thisNum) < lowest or lowest == -1: lowest = int(thisNum)

    #print("LINE LOWEST: " + str(lowest) + " HIGHEST: " + str(highest))
    sumTotal += highest - lowest

print("TOTAL: " + str(sumTotal))
