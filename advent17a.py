# Advent of Code 2017
# Day 17 - Part I
# mushmine - Python


'''
List/array insertion and then using modulo on the index to wrap it back to the beginning as necessary.
'''

puzzle_input = 328  # Num to skip
num_times = 2017 

# Test data!
# puzzle_input = 3
# num_times = 10

spinlock_list = [0]  # List that grows!
curr_pos = 0  # To keep track of current position.
for i in range(1, num_times + 1):  # Want the i to track loop iteration number. Start with 1, already a 0 in list.
    curr_pos = (curr_pos + puzzle_input) % len(spinlock_list)  # Using modulo to keep index within bounds of list.
    spinlock_list.insert(curr_pos + 1, i)
    curr_pos += 1

    # print("->", i, ":", " ".join([str(item) for item in spinlock_list]))

final_idx = spinlock_list.index(num_times) + 1  # Index of element after the num_times, per instructions.
print("VALUE AFTER", num_times, ":", spinlock_list[final_idx])