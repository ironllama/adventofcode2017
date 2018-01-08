# Advent of Code 2017
# Day 22 - Part I
# mushmine - Python


'''
The second part introduces 2 more states, weakened and flagged. The bulk of the logic is basically the same, with just the new states and the way they affect the facing direction.

Also, I changed the data structures for the tracking from lists into sets, because it was taking too long with lists (possibly HOURS, according to spit-ball estimates). We're doing mostly checks to see if values exist in the structure and the values were unique, so the speed advantage of sets was greatly appreciated and brought the execution time down to under 30 seconds.
'''

with open("advent22.in", "r") as f: all_list = f.readlines()
# all_list = ["..#","#..","..."]  # Test data!
# print("\n".join(all_list))

all_infected = set()  # NEW: Track all the infected coordinates as a set!
all_weakened = set()  # NEW: Track all the weakened coordinates as a set!
all_flagged = set()  # NEW: Track all the flagged coordinates as a set!

# Get all positions of infected squares.
for y in range(len(all_list)):
    for x in range(len(all_list[y])):
        if all_list[y][x] == "#": all_infected.add(str(x) + "," + str(y))
# print(all_infected)

curr_facing = "n"  # Starting by facing north.
curr_x = int(len(all_list) / 2)  # Find center.
curr_y = curr_x
# print ("CENTER:", curr_x, curr_y)

num_infected = 0
for i in range(10000000):
    # if curr_x < 0 or curr_y < 0: print("PROBLEM:", curr_x, curr_y)
    pos_str = str(curr_x) + "," + str(curr_y)

    if pos_str in all_infected:
        if curr_facing == "n": curr_facing = "e"
        elif curr_facing == "e": curr_facing = "s"
        elif curr_facing == "s": curr_facing = "w"
        elif curr_facing == "w": curr_facing = "n"
        all_infected.remove(pos_str)
        all_flagged.add(pos_str)
    elif pos_str in all_flagged:
        if curr_facing == "n": curr_facing = "s"
        elif curr_facing == "e": curr_facing = "w"
        elif curr_facing == "s": curr_facing = "n"
        elif curr_facing == "w": curr_facing = "e"
        all_flagged.remove(pos_str)
    elif pos_str in all_weakened:
        all_weakened.remove(pos_str)
        all_infected.add(pos_str)
        num_infected += 1
        # if num_infected % 100000 == 0: print("INFECTED:", num_infected)  # Spit-ball benchmarking.
    else:
        if curr_facing == "n": curr_facing = "w"
        elif curr_facing == "e": curr_facing = "n"
        elif curr_facing == "s": curr_facing = "e"
        elif curr_facing == "w": curr_facing = "s"
        all_weakened.add(pos_str)

    if curr_facing == "n": curr_y -= 1
    elif curr_facing == "e": curr_x += 1
    elif curr_facing == "s": curr_y += 1
    elif curr_facing == "w": curr_x -= 1

'''
The following is to print out the final matrix, for fun. Final result looked like a big wasp nest?
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