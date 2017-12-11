# Advent of Code 2017
# Day 11 - Part I
# mushmine - Python


'''The second part is surprisingly easy. We just have to calculate the distance at the end of every movement, rather than just once at the end. So, with Python, we just need to un-indent the end of our code and make sure we're tracking the highest distance ever calculated.'''

import math as math

with open("advent11a.txt", "r") as f:
    all_file = f.read().strip()

all_file_list = all_file.split(",")

curr_x = 0
curr_y = 0
furthest = 0  # NEW: Variable for tracking highest ever distance.

for this_dir in all_file_list:
    if this_dir == "n":
        curr_y += 1
    elif this_dir == "ne": 
        curr_x += 1
        if curr_x % 2 == 0: curr_y += 1
    elif this_dir == "se":
        curr_x += 1
        if curr_x % 2 == 1: curr_y -= 1
    elif this_dir == "s":
        curr_y -= 1
    elif this_dir == "sw":
        curr_x -= 1
        if curr_x % 2 == 1: curr_y -= 1
    elif this_dir == "nw":
        curr_x -= 1
        if curr_x %2 == 0: curr_y += 1

    # NEW: This block was brough into the loop, so that it's calculated every time we move.
    cube_x = curr_x
    cube_z = curr_y - (curr_x + (curr_x&1)) / 2
    cube_y = -cube_x - cube_z
    # print("CUBE x:", cube_x, "y:", cube_y, "z:", cube_z)

    final_distance = max(abs(cube_x), abs(cube_y), abs(cube_z))
    if final_distance > furthest: furthest = final_distance  # NEW: See if we need to update the furthest distance, so far.

print("FINAL DISTANCE:", final_distance)
print("FURTHEST:", furthest)
