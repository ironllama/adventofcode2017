# Advent of Code 2017
# Day 12 - Part II
# mushmine - Python


'''The second part builds on the first part. Since you know you can traverse the "pipes" and find what is connected to each other, now you have to find other groups. The way I approached it was to create a list of all possible nodes(numbers) -- easy, since all the lines numbers are sequential from 0 to 1999 for my problem set, and then as you encounter a node(number), you remove it from the list. So, this list becomes a list of numbers left to process. Then when you're finished with a group, you start with another number in this list of leftover nodes (I just pick whatever is at the beginning of the list) and start processing another group. All the while, I'm bumping up a tracking variable that's counting up.'''

with open("advent12a.txt", "r") as f:
    all_lines = f.readlines()

    # Test data!
    # all_lines = ["0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4", "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5"]

all_lines_list = []
for this_line in all_lines:
    this_line = this_line.strip()

    tokens_list = this_line.split(" ", 2)
    all_lines_list.append(tokens_list[2])

all_nums = list(range(len(all_lines)))  # NEW: Create the "leftover" node(numbers) list.
num_groups = 0  # NEW: Tracking number for total of groups found.

def traverseTree(this_branch):
    global root_connected
    # print("Checking:", this_branch, "root_connected:", root_connected)

    child_nodes = all_lines_list[this_branch].split(", ")
    for this_child in child_nodes:
        this_child = int(this_child)
        if this_child not in root_connected:
            root_connected.append(this_child)
            all_nums.remove(this_child)  # NEW: Remove the new number from the "leftover" node(numbers) list.
            traverseTree(this_child)

# NEW: Loop that will go through the "leftover" node(numbers) list until all the numbers are processed!
while len(all_nums) > 0:
    num_groups += 1  # Starting to process a new group!
    first_num = all_nums[0]  # Arbitrarily pick up the first element. Safest index, since this list is going to shrink!
    # print("STARTING WITH:", first_num)
    root_connected = [first_num]  # Initialize the list of connected nodes(numbers) with the first number.
    all_nums.remove(first_num)  # Remove it from the "leftover" node(numbers) list.
    traverseTree(first_num)  # Go, go, go!
    # print("SIZE all_nums:", len(all_nums))

print("TOTAL NUMBER OF GROUPD:", num_groups)
