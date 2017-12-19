# Advent of Code 2017
# Day 17 - Part II
# mushmine - Python


'''
Like the second part of Day 16, the second part of Day 17 asks for a ton of iterations. And again, just wrapping the original first part into a regular loop would take too long to generate the answer. So, I rewrote the program, looking for patterns. The only pattern I found in the output is that the 0 never moves, which makes sense because insertion always happens at current position + 1. So, the value we're looking for after the requisite 5000000 moves is the second number in the list (0 being the first.) Unless I'm mistaken about the simplicity of what we're looking for, we don't have to track all the data in the spinlock. I just loop through all the possible positions to insert, looking for any insertions into position 1, and track whatever that last number is/was.
'''

puzzle_input = 328  # Num to skip
num_times = 5000000 

# Test data!
# puzzle_input = 3
# num_times = 10

curr_pos = 0  # Current position we're calculating for.
next_to_zero = 0  # Tracking the last number that was inserted after the 0.
for i in range(1, num_times + 1):
    curr_pos = ((curr_pos + puzzle_input) % i) + 1
    if curr_pos == 1:  # If we inserted at position 1...
        next_to_zero = i  # Store this number.
        # print("FOUND:", i)

print("FINAL:", next_to_zero)
