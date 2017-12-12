# Advent of Code 2017
# Day 12 - Part I
# mushmine - Python


'''With this one, you have to follow a path based on the values encountered. Since you start with 0 and then are give a list of new paths to checkout after the "<->", you then have to follow each one of those paths (happen to line up as line numbers), each which lead to other paths (lines). There is a way of doing this with interation, but I decided to go with recursion, since it's easier for me to think about. Basically, I create a function that takes a line number and then gets the list of lines that are connected to it, and then calls itself with each of those lines. There is the possibility of runaway recursion (infinite loops) and stack overflow, so you have to be a bit careful, depending on your programming language's ability to handle those. Python is pretty good with giving you a warning if you start to get too out there.'''

with open("advent12a.txt", "r") as f:
    all_lines = f.readlines()  # Read each line of file as an element in a list.

    # Test data!
    # all_lines = ["0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4", "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5"]

all_lines_list = []  # Going to create another list that only contains the stuff to the right of the <-> on each line.
for this_line in all_lines:
    this_line = this_line.strip()  # Removes the newlines, if any.

    tokens_list = this_line.split(" ", 2)  # Splits the line by the space, but only twice. For example: ["2", "<->", "0, 3, 4"]
    all_lines_list.append(tokens_list[2])  # Only care what's after the <->, and stick it into the new list.

root_connected = [0]  # Since we're starting with 0, gonna add it as a connected node in the list.
def traverseTree(this_branch):  # Going to recursively call this function with each node(line number) encountered!
    global root_connected  # Since we're changing the global variable.
    # print("Checking:", this_branch, "root_connected:", root_connected)

    child_nodes = all_lines_list[this_branch].split(", ")  # Get each line list (string), and split it by the commas.
    for this_child in child_nodes:  # For each node(line number)...
        this_child = int(this_child)  # Cast into integer to use as an index number, later.
        if this_child not in root_connected:  # If it doesn't already exist in the list of things connected to root...
            root_connected.append(this_child)  # Add it to the list.
            traverseTree(this_child)  # Check out it's own list of connected nodes(line numbers).

traverseTree(0)  # This kicks it all off, starting with the node(line number) 0.
print("TOTAL NUMBER OF PROGRAMS:", len(root_connected))
