# Advent of Code 2017
# Day 4 - Part II
# Python


''' The strategy for this one was pretty much the same as Part I: to get each line from the puzzle
input, and then separate each line into a list of separate words. Then just loop through each word
in the list and test against other words in the list that proceeding it. If any words match, then
the line is deemed invalid and the loop continues to the next line of words.

The testing between words on a line are to see if they are anagrams. To actually test if words are
anagrams is pretty tough if you are going to test each possibility manually. To get the same effect,
and a bit more efficiently, one can rearrange all the letters of each word alphabetically and then
see if the letters are the same for each word.'''

f = open("day4a.txt")
allLinesList = f.readlines()  # Read from file as lines into a list of lines!

# print("TOTAL LINES: ", len(allLinesList))
numValid = 0  # Going to keep track of our target number with this.

for thisLine in allLinesList:  # For each line in the puzzle input.
    thisLineList = thisLine.strip().split(" ")  # Strip new line at the end and split into individual words.
    # print(thisLineList)
    valid = True  # Track whether this line is a valid line.

    for i in range(len(thisLineList) - 1):  # For each word in the line list, except last one.
        thisWord = thisLineList[i]  # For convenience, give the current word a nice var name.
        thisWordList = list(thisWord)  # Convert the word into a list of characters.
        thisWordList.sort()  # Sort the list of characters.
        thisWord = ''.join(thisWordList)  # Join the characters back into a word.
        # print("WORD: ", thisWord)
        for j in range(i + 1, len(thisLineList)):  # Loop against other words in the line.
            thatWord = ''.join(sorted(list(thisLineList[j]))) # Same as lines 23-26, but all at once.
            # print("TESTING: [", thisWord, "] AND [", thatWord, "]")
            if thisWord == thatWord:
                # print("DUPES! [" + thisWord + "][" + thisLineList[match] + "]")
                valid = False
                break  # No point testing the rest of the words in the line against thisWord.
        if valid == False: break  # No point testing the rest of the line.
    
    # This is evaulated if it processed every word in the line, or broke out early.
    if valid == True: numValid += 1 

print("LINES VALID: ", numValid)
