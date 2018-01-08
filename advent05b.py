# Advent of Code 2017
# Day 5 - Part II
# Python


''' Same as Part I, but with different processing of the instruction at the cursor. I've eliminated
most of the comments for lines that were exactly the same as Part I but not new lines, so refer to
Part I for those comments.'''

with open("advent05.in") as f:
    allLinesList = f.read().splitlines()
    # allLinesList = ["0", "3", "0", "1", "-3"]
    allLinesList = [int(thisLine) for thisLine in allLinesList]

currPos = 0
numInstructions = 0

while currPos >=0 and currPos <= len(allLinesList) - 1:
    numInstructions += 1
    thisInstruction = allLinesList[currPos]

    # NEW: Implementation of new directions, for new special case where jump is 3 or more!
    # Note that the instructions don't make it clear what happens if jump is -3 or less.
    if thisInstruction >= 3: allLinesList[currPos] -= 1
    else: allLinesList[currPos] += 1

    currPos += thisInstruction
    # print("#:", numInstructions, " INSTR:", thisInstruction, " NEWPOS:", currPos)
    # print("ARRAY: ", allLinesList)

print("BROKE OUT AFTER: ", numInstructions)
