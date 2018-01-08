# Advent of Code 2017
# Day 24 - Part I
# mushmine - Python


'''
For this one, I thought that since it was an indeterminate traversal through the data, I'd use a recursive function. My version does not take into account the shorter variations of larger paths. For example, if there is a path A->B->C->D, I don't care about A->B->C or A->B or A, since there are longer path with those pieces and we're only interseted in the largest total value for paths, which seem to suggest we need to total up only the longest path variations.
'''

with open("advent24a.txt", "r") as f: all_lines_list = f.readlines()
# all_lines_list = ["0/2", "2/2", "2/3", "3/4", "3/5", "0/1", "10/1", "9/10"]  # Test data!

starting_list = []  # To track which ports are starting ports, or have a port that is 0.
all_components = []  # To track all available ports.
valid_paths = []  # To track all resulting long, valid paths.

# First, we process all the lines from the input data.
for this_line in all_lines_list:
    ports = this_line.strip().split("/")  # Strip each line of newlines and separate by the slash.
    all_components.append(ports)  # Add this pair to the all_components list. (Could also use a tuple?)
    if ports[0] == "0" or ports[1] == "0": starting_list.append(ports)  # Save the ones that have 0 as port!

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


# Iterate through the starting_list of pairs and start traversing down possible paths.
for this_pair in starting_list:
    # We should remove this port combo from the list, so it does not reuse it as a possible future path.
    new_list = [elem for elem in all_components if elem != this_pair]

    # Start going down all possible paths! As this goes through them, it'll fill up the valid_paths list.
    traverse_components(this_pair[1], [this_pair], new_list)


largest_path = ""
largest_path_val = 0
for this_path in valid_paths:  # Now, just go through the valid_paths and find the one with largest total.
    total = 0
    for this_pair in this_path: total += int(this_pair[0]) + int(this_pair[1])  # Total up the path.
    if total > largest_path_val:  # If it's the largest total, track it.
        largest_path_val = total
        largest_path = this_path
    # print(this_path, total)

print("LARGEST PATH:", " ".join("/".join(this_pair) for this_pair in largest_path))
print("VALUE:", largest_path_val)