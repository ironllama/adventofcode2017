# Advent of Code 2017
# Day 9 - Part I
# mushmine - Python


'''Process each letter to determine shift in state, whether currently in a garbage state or an ignoring-next-char state. While doing that, keep track of how deep each of the brackets are nested, and use that depth level to add up the different blocks (groups) in the stream of characters. There was a bit of mental effort before coding to organize the different possible states. (Probably best on paper -- there's quite a few possible shifts to optimize.'''

with open("advent09a.txt", "r") as f:
    all_lines_str = f.read().strip()

    # Test data!
    # all_lines_str = "{}"  # 1
    # all_lines_str = "{{{}}}"  # 6
    # all_lines_str = "{{},{}}"  # 5
    # all_lines_str = "{{{},{},{{}}}}"  # 16
    # all_lines_str = "{<a>,<a>,<a>,<a>}"  # 1
    # all_lines_str = "{{<ab>},{<ab>},{<ab>},{<ab>}}"  # 9
    # all_lines_str = "{{<!!>},{<!!>},{<!!>},{<!!>}}"  # 9
    # all_lines_str = "{{<a!>},{<a!>},{<a!>},{<ab>}}"  # 3

ignore_next = False  # Track whether to ignore the next character.
in_garbage = False  # Track of whether we're currently looking at stuff in garbage.
bracket_depth = 0  # To track how far nested the current group is.
total_so_far = 0  # To track the total, since they want the groups added up.

for this_char in all_lines_str:  # Loop through each character!
    # print("[", this_char, "] IGNORE[", ignore_next, "GARBAGE[", in_garbage, "] DEPTH[", bracket_depth, "] TOTAL[", total_so_far, "]")

    if ignore_next: ignore_next = False  # If we're ignoring this character, then just toggle the flag off and nothing more.
    else:
        if this_char == "!": ignore_next = True  # Current character is a !, so ignore the next char! (Even in garbage state.)
        else:
            if in_garbage:
                # If the non-ignored non-garbaged state char is a >, then we're finished with the garbage state!
                if this_char == ">": in_garbage = False
            else:
                if this_char == "<": in_garbage = True  # Start the garbage state!
                if this_char == "{": bracket_depth += 1  # Going deeper into a nested group. Level up!
                elif this_char == "}":
                    # Finished with a group level, so increment the total, and decrement the nested group counter.
                    total_so_far += bracket_depth
                    bracket_depth -= 1

print("TOTAL SCORE FOR GROUPS:", total_so_far)