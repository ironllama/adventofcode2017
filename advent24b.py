# Advent of Code 2017
# Day 24 - Part II
# mushmine - Python


'''
Nothing changes in the finding of the valid longest path variations, it's just that instead of finding the largest total value, we're looking for the actual longest length or number of pairs. However, since we still resolve ties with total values of the paths, we still use the existing code to resolve these ties.

(We could have also included the test for longest paths inside the recursive function, while we're looking for the paths. Wanted to keep the recursive function simple, though.)
'''

with open("advent24.in", "r") as f: all_lines_list = f.readlines()
# all_lines_list = ["0/2", "2/2", "2/3", "3/4", "3/5", "0/1", "10/1", "9/10"]  # Test data!

starting_list = []
all_components = []
valid_paths = []

for this_line in all_lines_list:
    ports = this_line.strip().split("/")
    all_components.append(ports)
    if ports[0] == "0" or ports[1] == "0":
        starting_list.append(ports)

def traverse_components(from_here, full_path, in_components):
    # print("traverse_component", from_here, full_path, in_components)
    value = 0
    found = False
    for this_pair in in_components:
        if this_pair[0] == from_here:
            found = True
            new_list = [elem for elem in in_components if elem != this_pair]
            new_path = list(full_path)
            new_path.append(this_pair)
            traverse_components(this_pair[1], new_path, new_list)
        elif this_pair[1] == from_here:
            found = True
            new_list = [elem for elem in in_components if elem != this_pair]
            new_path = list(full_path)
            new_path.append(this_pair)
            traverse_components(this_pair[0], new_path, new_list)
    if not found: valid_paths.append(full_path)

for this_pair in starting_list:
    new_list = [elem for elem in all_components if elem != this_pair]
    traverse_components(this_pair[1], [this_pair], new_list)

# NEW: Now, first we determine which of the resulting paths are the longest overall.
longest_paths = []  # To track longest path, but there may be more than one of the same length!
longest_path_len = 0
for this_path in valid_paths:
    if len(this_path) > longest_path_len:  # New longest? Then overwrite the tracking list.
        longest_path_len = len(this_path)
        longest_paths = [this_path]
    elif len(this_path) == longest_path_len:  # If the same length, add to tracking list.
        longest_paths.append(this_path)
# print("LONGEST:", longest_path_len)
# print("NUMBER OF PATHS THAT HAVE LONGEST LENGTH:", len(longest_paths))

strongest_path = []
strongest_path_val = 0
for this_path in longest_paths:
    total = 0
    for this_pair in this_path:
        total += int(this_pair[0]) + int(this_pair[1])
    if total > strongest_path_val:
        strongest_path_val = total
        strongest_path = this_path
    # print(this_path, total)

print("STRONGEST PATH:", strongest_path)
print("VALUE:", strongest_path_val)