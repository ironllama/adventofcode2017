# Advent of Code 2017
# Day 9 - Part II
# mushmine - Python


''' The only real difference with this one, is that we have to track the garbage. Given our current method of reading through the characters as they come in, is pretty straightforward! Yay! (Removed some of the code tracking levels and total of group levels.)'''

with open("advent09.in", "r") as f:
    all_lines_str = f.read().strip()

    # Test data!
    # all_lines_str = "<>"  # 0
    # all_lines_str = "<random characters>"  # 17
    # all_lines_str = "<<<<>"  # 3
    # all_lines_str = "<{!>}>"  # 2
    # all_lines_str = "<!!>"  # 0
    # all_lines_str = "<!!!>>"  # 0
    # all_lines_str = '<{o"i!a,<{i<a>'  # 10

ignore_next = False
in_garbage = False
non_cancelled_garbage = 0  # NEW: Tracking the number of non-ignored garbage characters!

for this_char in all_lines_str:
    # print("[", this_char, "] IGNORE[", ignore_next, "GARBAGE[", in_garbage, "] DEPTH[", bracket_depth, "] TOTAL[", total_so_far, "]")

    if ignore_next: ignore_next = False
    else:
        if this_char == "!": ignore_next = True
        else:
            if in_garbage:
                if this_char == ">": in_garbage = False
                else: non_cancelled_garbage += 1  # NEW: If the garbage char is not a >, it's counted as a garbage char!
            else:
                if this_char == "<": in_garbage = True

print("TOTAL NON_CANCELLED_GARBAGE:", non_cancelled_garbage)
