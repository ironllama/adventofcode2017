# Advent of Code 2017
# Day 6 - Part II
# mushmine - Python


'''Fortunately, not much to change in Part II. Decided to let the loop store the final combo, so that I can know which state
pattern in history was the one that repeated. (The last one!)'''

with open("advent06.in") as f:
    allNumsList = f.read().split("\t")
    # allNumsList = ["0", "2", "7", "0"]

    allNumsList = [int(thisStr) for thisStr in allNumsList]

history = [ "-".join(map(str, allNumsList)) ]

while True:
    largest_idx = 0

    for i in range(len(allNumsList)):
        thisNum = allNumsList[i]
        if thisNum > allNumsList[largest_idx]: largest_idx = i

    largest_val = allNumsList[largest_idx]
    allNumsList[largest_idx] = 0

    for i in range(largest_val):
        next_idx = (largest_idx + i + 1) % len(allNumsList) 
        allNumsList[next_idx] += 1

    new_pattern = "-".join(map(str, allNumsList))

    # NEW: Instead of breaking out before finding the repeat, this time we write the repeating one into the list!
    # We still need to test for a repeating pattern before adding, else every pattern will be found in the list (at the end
    # where we just added it!) So, another boolean variable to keep track as we test and add to the list afterwards.
    found = False  
    if new_pattern in history: found = True

    history.append(new_pattern)

    if found: break  # If there is a repeat, then break out of the infinite loop!

final_idx = len(history) - 1  # The last state is the one that repeated and so the one we're looking for in history before it!
print("LOOKING FOR:", history[final_idx])

idx_first_occur = history.index(history[final_idx])  # Simple index() function to find the position of it.
print("IDX: ", idx_first_occur)

print("NUM CYCLES BETWEEN REPEATS:", final_idx - idx_first_occur)  # Then just math to see how many steps in between!
