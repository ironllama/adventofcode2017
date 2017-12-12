# Advent of Code 2017
# Day 6 - Part I
# mushmine - Python


'''Lots of array/list manipulation in this one. One array that keeps changing, and another array that keeps growing as a kind
of ledger to check for a repeating combination of list elements. I ended up just creating a string out of the ever changing
list states and then seeing if any new strings matched old ones with a simple 'if in' control statement.'''

with open("advent06a.txt") as f:  # Reading in from file for puzzle inputs.
    allNumsList = f.read().split("\t")  # Read file as a big string, then split into list by tabs.
    # allNumsList = ["0", "2", "7", "0"]  # Test array!

    allNumsList = [int(thisStr) for thisStr in allNumsList]  # Turn list of strings into list of integers.

history = [ "-".join(map(str, allNumsList)) ]  # Keeping track of allNumsList's previous states as strings in here.
# The map() function to copy the integer list into a string list for joining. Was thinking of keep it as a string list,
# but there's so much more number/math manipulation in the main loop coming up!

while True:
    largest_idx = 0  # To keep track of the largest number in the memory banks.

    for i in range(len(allNumsList)):  # Find the largest bank!
        thisNum = allNumsList[i]  # Convenience.
        if thisNum > allNumsList[largest_idx]: largest_idx = i

    largest_val = allNumsList[largest_idx]  # Store value before emptying bank in next statement.
    allNumsList[largest_idx] = 0  # Empty the bank!

    for i in range(largest_val):  # Redistribute the amount in the bank!
        next_idx = (largest_idx + i + 1) % len(allNumsList)  # Starting with the next bank, keep going, wrapping as necessary.
        allNumsList[next_idx] += 1  # Everybody gets 1!

    new_pattern = "-".join(map(str, allNumsList))  # Take a string snapshot of the new state of allNumList!
    # print("NEW_PATTERN:", new_pattern)

    if new_pattern in history:  # If it's a state we've seen before, we can stop.
        break

    history.append(new_pattern)  # Otherwise, store the state and keep going!
    # print("HISTORY:", history)

# print("FINAL HISTORY:", history)
print("NUM REALLOCATION CYCLES:", len(history))
