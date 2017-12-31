with open("advent22a.py", "r") as f: all_list = f.readlines()
# all_list = ["..#","#..","..."]
# print("\n".join(all_list))

all_infected = []  # Track all the infecrted coordinates.

# Get all positions of infected squares.
for y in range(len(all_list)):
    for x in range(len(all_list[y])):
        if all_list[y][x] == "#": all_infected.append(str(x) + "," + str(y))
# print(all_infected)

curr_facing = "n"  # Starting by facing north.
curr_x = int(len(all_list) / 2)  # Find center.
curr_y = curr_x
# print ("CENTER:", curr_x, curr_y)

num_infected = 0
for i in range(10000):
    # if curr_x < 0 or curr_y < 0: print("PROBLEM:", curr_x, curr_y)
    pos_str = str(curr_x) + "," + str(curr_y)

    if pos_str in all_infected:
        if curr_facing == "n": curr_facing = "e"
        elif curr_facing == "e": curr_facing = "s"
        elif curr_facing == "s": curr_facing = "w"
        elif curr_facing == "w": curr_facing = "n"
        all_infected.remove(pos_str)
    else:
        if curr_facing == "n": curr_facing = "w"
        elif curr_facing == "e": curr_facing = "n"
        elif curr_facing == "s": curr_facing = "e"
        elif curr_facing == "w": curr_facing = "s"
        all_infected.append(pos_str)
        num_infected += 1

    if curr_facing == "n": curr_y -= 1
    elif curr_facing == "e": curr_x += 1
    elif curr_facing == "s": curr_y += 1
    elif curr_facing == "w": curr_x -= 1

# max_dim = 0
# for this_infected in all_infected:
#     this_coord = this_infected.split(",")
#     this_x = abs(int(this_coord[0]))
#     this_y = abs(int(this_coord[1]))
#     if int(this_x) > max_dim: max_dim = int(this_x) + 1
#     if int(this_y) > max_dim: max_dim = int(this_y) + 1
# print("MAX_DIM:", max_dim)

# print("BEFORE:", all_infected)
# num_infected = 0
# for y in range(max_dim * 2):
#     for x in range(max_dim * 2):
#         this_coord = str(x - int(max_dim / 2)) + "," + str(y - int(max_dim / 2))
#         # print("NEW:", this_coord)
#         if this_coord in all_infected:
#             print("#", end="")
#             num_infected += 1
#         else: print(".", end="")
#     print("")

print("ANSWER:", num_infected)