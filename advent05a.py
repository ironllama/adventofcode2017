# Advent of Code 2017
# Day 5 - Part I
# Python


'''The linear nature of the problem makes this logically rather straightforward. Each of the lines in
the file are a single number, which gives further instructions. So, we basically read each line and
after processing, go to another line. Since we may not necessarily read every line, and certainly not
in order, it's a pretty good candidate for a while loop.'''

with open("day5a.txt") as f:  # Cleaner and better way to read/write files using with!
    # Read file as a big string, then split into list by newlines.
    # Did this instead of just readlines(), because we also want to rid of the newline on each line.
    allLinesList = f.read().splitlines()
    # allLinesList = ["0", "3", "0", "1", "-3"]  # Test data. Comment above and use this for testing.

    # Convert to list of strings into list of ints for our program. List comprehensions ftw!
    allLinesList = [int(thisLine) for thisLine in allLinesList]

currPos = 0  # To keep track of the currently processing position in the list. Aka, a cursor.
numInstructions = 0  # To keep track of how many instructions we've processed, so far.

while currPos >= 0 and currPos <= len(allLinesList) - 1:  # While we're still in the range of the list.
    numInstructions += 1
    thisInstruction = allLinesList[currPos]  # Store the current instruction, before bumping it up.
    allLinesList[currPos] += 1  # Bump up the instruction by 1, afrter we've read it.
    currPos += thisInstruction  # Use the original instruction to move the currPos, or cursor.
    # print("#:", numInstructions, " INSTR:", thisInstruction, " NEWPOS:", currPos)
    # print("ARRAY: ", allLinesList)  # Don't use this for the huge problem set.

print("BROKE OUT AFTER: ", numInstructions)
