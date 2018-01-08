# Advent of Code 2017
# Day 19 - Part II
# mushmine - Python


'''
Added a variable to track the number of cycles in our loop. That's it!
'''

with open("advent19.in", "r") as f: lines_list = f.readlines()

# Test data!
# # lines_list = ["     |          ", "     |  +--+    ", "     A  |  C    ", " F---|----E|--+ ", "     |  |  |  D ", "     +B-+  +--+ "]

curr_x = lines_list[0].index("|")
curr_y = 0
curr_dir = "s"

final_str = ""
num_steps = 0  # NEW: To track the number of steps taken until the end.
while True:
    curr_char = lines_list[curr_y][curr_x]  # Get this next char!
    # print("LOOP curr_char:", curr_char, "x:", curr_x, "y:", curr_y, "dir:", curr_dir)

    if curr_char == "+":

        if curr_dir == "n" or curr_dir == "s":
            if lines_list[curr_y][curr_x + 1] != " ": curr_dir = "e"
            elif lines_list[curr_y][curr_x - 1] != " ": curr_dir = "w"
        elif curr_dir == "e" or curr_dir == "w":
            if lines_list[curr_y - 1][curr_x] != " ": curr_dir = "n"
            elif lines_list[curr_y + 1][curr_x] != " ": curr_dir = "s"

    elif curr_char.isalpha(): final_str += curr_char

    elif curr_char == " " or curr_y < 0 or curr_x < 0: break

    if curr_dir == "n": curr_y -= 1
    elif curr_dir == "e": curr_x += 1
    elif curr_dir == "s": curr_y += 1
    elif curr_dir == "w": curr_x -= 1

    num_steps += 1  # NEW: Increment the number of steps taken.

print("FINAL:", final_str, "NUM_STEPS:", num_steps)
