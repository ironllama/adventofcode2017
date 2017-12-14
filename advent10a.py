# Advent of Code 2017
# Day 10 - Part I
# mushmine - Python


'''This was not too bad -- the directions were fairly clear what was going to happen and the examples were helpful. Basically, we're taking a string input and converting it into a list of integers to use as "lengths". The actual list of numbers that gets operated on is a separate list that just starts out 0 through 255. Extracting the length you needed top copy out of the numbers list and reversing it wasn't too bad. However, sticking the reversed numbers back into the numbers list made me pause a bit. There's not really a way of doing it as a chunk of data, as far as I know, except for creating a new list of the reversed data and the untouched data built back up around it. So, instead of trying to do it as a whole, I decided to loop through each number of the reversed list and place them back into the numbers list one at a time. With the current position being tracked and always pointing at where we started the initial extraction, this made the most sense. The second challenge was one that we've encountered quite a few times in this year's puzzles: wrapping list indexes back around to the beginning. Fortunately, there is a trick for doing this with modulo -- look up what modulo does if you are not already familiar with what it does. We are using it to keep a value WITHIN the bounds of a range of numbers. For example, "x % 25" will always keep x within 0-24, because the least the remainder can be is 0 and the most the remainder can be will be 24. (25 % 25 is 0) Similarly, "x % 256" will keep x between 0 and 255! Neato!'''

input = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"  # My puzzle input. Yours could be different!
nums_list = [x for x in range(0, 256)]  # Initialize the list of numbers 0-255.

# Test set of inputs and num list.
# input = "3,4,1,5"
# nums_list = [x for x in range(0, 5)]

curr_pos = 0  # Track current position in numbers list.
skip_size = 0  # Track the number of positions to skip every time through the loop.

input_list = [int(thisChar) for thisChar in input.split(",")]  # Turn the list of strings into a list of integers.

for this_range in input_list:  # Get each number from the input list, and call it this_range.
    # print("INPUT:", this_range, "CURSOR:", curr_pos, "SKIP:", skip_size, "NUMS_LIST:", nums_list)
    temp_list = []  # Temporary list to store our extracted set of numbers. We need to reverse these, later.

    # Find and extract our numbers, one number at a time. Start using the curr_pos, and extract as many as in this_range.
    for j in range(curr_pos, curr_pos + this_range):
        nums_list_idx = j % len(nums_list)  # The index of the next number to extract. (Using modulo to wrap back around.)
        temp_list.append(nums_list[nums_list_idx])  # Store this new number in the temp_list.

    temp_list.reverse()  # So easy!

    # Now we have to stick the reversed temp list back in place. Process each number, one at a time.
    for j in range(len(temp_list)):  # For each number in the temp list...
        nums_list_idx = (curr_pos + j) % len(nums_list)  # Index of the num_list where we put the number. (Modulo to wrap.)
        nums_list[nums_list_idx] = temp_list[j]
    
    # Then advance the current position (curr_pos) and skip size, per instructions.
    curr_pos = (curr_pos + this_range + skip_size) % len(nums_list)  # Using modulo to wrap back around.
    skip_size += 1
    # print("END LOOP - NUMS_LIST:", nums_list)

# print(nums_list)
print("PRODUCTS OF FIRST TWO:", nums_list[0] * nums_list[1])