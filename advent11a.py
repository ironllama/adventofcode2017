# Advent of Code 2017
# Day 11 - Part I
# mushmine - Python


'''Another puzzle where you learn new ways of approaching data and traversal! The hex grid is pretty interesting -- I've certainly used while playing games, but this is the first time I've had to actually figure out how it works. Anyway, part of figuring out this puzzle is understanding hdex grids, and for that I fired up Google and looked up some resources. One of the good ones, and the one I used to help me create this solution is:

https://www.redblobgames.com/grids/hexagons/

I used the even-q vertical layout, because that seemed the closest to the standard coordinate system I'm used to. However, I had to flip it so that X values went higher as you went up, which is opposite of what their diagrams have. For distance, it doesn't matter, but I like my positives on the upper right quadrant! To make it even more clean, I actually drew out the grid I wanted and them numbered them accordinly. This helped me look for patterns in how X and Y changed as I moved around the grid. Then when calculating distance, I took their advice and changed the X,Y offset coordinates that I'm used to and converted it into cubic coordinates using their helpful little code snippet and then used their cube distance snippet.
'''

import math as math

with open("advent11a.txt", "r") as f:
    all_file = f.read().strip()

    # Test data!
    # all_file = "ne,ne,ne"
    # all_file = "ne,ne,sw,sw"
    # all_file = "ne,ne,s,s"
    # all_file = "se,sw,se,sw,sw"
    # all_file = "se,s,s,sw,se,ne,s,ne,n,ne,nw,s,s,s,ne,ne,nw"

all_file_list = all_file.split(",")

# To track current position, using X and Y coordinates.
curr_x = 0
curr_y = 0

for this_dir in all_file_list:  # For each instruction in the all_file_list, change X and Y as necessary!
    if this_dir == "n":
        curr_y += 1
    elif this_dir == "ne": 
        curr_x += 1
        if curr_x % 2 == 0: curr_y += 1  # I noticed on my drawings that Y changed only on even X's.
    elif this_dir == "se":
        curr_x += 1
        if curr_x % 2 == 1: curr_y -= 1  # I noticed on my drawings that Y changed only on odd X's. 
    elif this_dir == "s":
        curr_y -= 1
    elif this_dir == "sw":
        curr_x -= 1
        if curr_x % 2 == 1: curr_y -= 1  # I noticed on my drawings that Y changed only on odd X's.
    elif this_dir == "nw":
        curr_x -= 1
        if curr_x %2 == 0: curr_y += 1  # I noticed on my drawings that Y changed only on even X's.

    # print("DIR:", this_dir, "X:", curr_x, "Y:", curr_y)

# Turn the offset coordinates into cubic coordinates to get ready to calculate cubic distance!
cube_x = curr_x
cube_z = curr_y - (curr_x + (curr_x & 1)) / 2  # The '&1' gets the first binary bit to determine even/odd.
cube_y = (-cube_x) - cube_z
# print("CUBE x:", cube_x, "y:", cube_y, "z:", cube_z)

final_distance = max(abs(cube_x), abs(cube_y), abs(cube_z))  # Very easy with cubic coordinates!
print("FINAL DISTANCE:", final_distance)
