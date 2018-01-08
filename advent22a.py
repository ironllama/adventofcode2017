# Advent of Code 2017
# Day 22 - Part I
# mushmine - Python


'''
For this puzzle, I initially thought about actually creating a multi-dimensional list, where each position tracks its own current state. However, it looks like the list would need to grow over time at an arbitrary rate, if the position goes outside the bounds of the current multi-dimensional list. So, instead of wrangling a large matrix that grows over time, I thought it would be easier to just have a list of infected positions.
'''

with open("advent22.in", "r") as f: all_list = f.readlines()
# all_list = ["..#","#..","..."]  # Test data!
# print("\n".join(all_list))

all_infected = []  # Track all the infected coordinates.

# Get all positions of infected squares.
for y in range(len(all_list)):
    for x in range(len(all_list[y])):
        if all_list[y][x] == "#": all_infected.append(str(x) + "," + str(y))
# print(all_infected)

curr_facing = "n"  # Starting by facing north.
curr_x = int(len(all_list) / 2)  # Find center.
curr_y = curr_x
# print ("CENTER:", curr_x, curr_y)

num_infected = 0  # Track the number of times infection occurred.
for i in range(10000):
    # if curr_x < 0 or curr_y < 0: print("PROBLEM:", curr_x, curr_y)
    pos_str = str(curr_x) + "," + str(curr_y)  # String position.

    if pos_str in all_infected:
        # First, change direction it's facing.
        if curr_facing == "n": curr_facing = "e"
        elif curr_facing == "e": curr_facing = "s"
        elif curr_facing == "s": curr_facing = "w"
        elif curr_facing == "w": curr_facing = "n"

        # Then, toggle infection.
        all_infected.remove(pos_str)  # If currently infected, make clean.
    else:
        # First, change direction it's facing.
        if curr_facing == "n": curr_facing = "w"
        elif curr_facing == "e": curr_facing = "n"
        elif curr_facing == "s": curr_facing = "e"
        elif curr_facing == "w": curr_facing = "s"

        # Then, toggle infection.
        all_infected.append(pos_str)  # If currently clean, make infected.
        num_infected += 1  # Increment number by 1!

    # Last, move forward by 1, in the direction it's facing.
    if curr_facing == "n": curr_y -= 1
    elif curr_facing == "e": curr_x += 1
    elif curr_facing == "s": curr_y += 1
    elif curr_facing == "w": curr_x -= 1

'''
The following is to print out the final matrix, for fun. Final result looked like a rabbit dangling at the end of a stick? Or maybe a hobo stick with sack of stuff? Or maybe it's nothing and any resemblance is coincidence?
'''
# max_dim = 0
# for this_infected in all_infected:
#     this_coord = this_infected.split(",")
#     this_x = abs(int(this_coord[0]))
#     this_y = abs(int(this_coord[1]))
#     if int(this_x) > max_dim: max_dim = int(this_x) + 1
#     if int(this_y) > max_dim: max_dim = int(this_y) + 1
# print("MAX_DIM:", max_dim)

# print("BEFORE:", all_infected)
# for y in range(max_dim * 2):
#     for x in range(max_dim * 2):
#         this_coord = str(x - int(max_dim / 2)) + "," + str(y - int(max_dim / 2))
#         # print("NEW:", this_coord)
#         if this_coord in all_infected:
#             print("#", end="")
#         else: print(".", end="")
#     print("")

print("ANSWER:", num_infected)