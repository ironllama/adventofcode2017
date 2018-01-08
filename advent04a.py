# Advent of Code 2017
# Day 4 - Part I
# Python


''' The strategy for this one was to get each line from the puzzle input, and then separate each line
into a list of separate words. Then just loop through each word in the list to see if any other word
in the list matches any proceeding word in the list. If any words match, then the line is deemed
invalid and the loop continues to the next line of words.'''

f = open("advent04.in")
allLinesList = f.readlines()  # Read from file as lines into a list of lines!

# print("TOTAL LINES: ", len(allLinesList))
numValid = 0  # Going to keep track of our target number with this.

for thisLine in allLinesList:  # For each line in the puzzle input.
    thisLineList = thisLine.strip().split(" ")  # Strip new line at the end and split into individual words.
    # print(thisLineList)
    valid = True  # Track whether this line is a valid line.

    for i in range(len(thisLineList) - 1):  # For each word in the line list, except last one.
        thisWord = thisLineList[i]  # For convenience, give the current word a nice var name.

        # The index function (Python 3.5+) can throw a ValueError if it doesn't find its target. So,
        # we need to use a try/except structure to contain the possible Error.
        try:
            # print("TESTING: [" + thisWord + "]")
            # The variable match is a throwaway. The second parameter is an offset -- everything after
            # the current word we're processing.
            match = thisLineList.index(thisWord, i + 1)
        except ValueError:
            continue  # If it doesn't find a match, then contine to next word on line
        else:
            # print("DUPES! [" + thisWord + "][" + thisLineList[match] + "]")
            valid = False
            break  # No point looking at the rest of the words in the line!

    # This is evaulated if it processed every word in the line, or broke out early.
    if valid == True: numValid += 1

print("LINES VALID: ", numValid)
