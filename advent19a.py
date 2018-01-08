# Advent of Code 2017
# Day 19 - Part I
# mushmine - Python


'''
This one I used my usual multidimensional list to store the map and the traversed the list, based on the characters encountered. The traversal loop was seeded with the "|" that was supposed to be at the "top" of the list. I like values that go south to go down, like in a Cartesian coordinate system, but since this one didn't seem to go back through the X axis, I stuck with the example and let the values go south go up.

 0123456789...
0     |          
1     |  +--+    
2     A  |  C    
3 F---|----E|--+ 
4     |  |  |  D 
5     +B-+  +--+ 

So, in my solution, the puzzle starts at (5,0) and then moves down to (5,1) then (5,2), etc. When it encounters the "+", it looks left and right to see which side has the non-blank line to follow. Fortunately, the data doesn't have a "+" junction right next to a parallel path (at least one space between parallel paths), so just looking for a non-blank direction sufficed.
'''

with open("advent19.in", "r") as f: lines_list = f.readlines()

# Test data!
# lines_list = ["     |          ", "     |  +--+    ", "     A  |  C    ", " F---|----E|--+ ", "     |  |  |  D ", "     +B-+  +--+ "]

# Seed with starting position and direction.
curr_x = lines_list[0].index("|")
curr_y = 0
curr_dir = "s"

final_str = ""  # To track all the letters we encounter on the way.
while True:
    curr_char = lines_list[curr_y][curr_x]  # Get this next char!
    # print("LOOP curr_char:", curr_char, "x:", curr_x, "y:", curr_y, "dir:", curr_dir)

    if curr_char == "+":  # When hitting a junction, we need to look around to see where to go next. (Change current direction.)

        if curr_dir == "n" or curr_dir == "s":  # From 'n' or 's', we have to choose to go 'e' or 'w'
            if lines_list[curr_y][curr_x + 1] != " ": curr_dir = "e"
            elif lines_list[curr_y][curr_x - 1] != " ": curr_dir = "w"
        elif curr_dir == "e" or curr_dir == "w":  # From 'e' or 'w', we have to choose to go 'n' or 's'
            if lines_list[curr_y - 1][curr_x] != " ": curr_dir = "n"
            elif lines_list[curr_y + 1][curr_x] != " ": curr_dir = "s"

    elif curr_char.isalpha(): final_str += curr_char  # If we hit a letter, then store it!

    elif curr_char == " " or curr_y < 0 or curr_x < 0: break  # If we hit a blank or leave the valid area, exit out.

    # Depending on our current direction, we need to move to adjacent X or Y.
    if curr_dir == "n": curr_y -= 1
    elif curr_dir == "e": curr_x += 1
    elif curr_dir == "s": curr_y += 1
    elif curr_dir == "w": curr_x -= 1


print("FINAL:", final_str)