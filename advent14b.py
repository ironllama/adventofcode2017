# Advent of Code 2017
# Day 14 - Part II
# mushmine - Python


'''
Part II builds on Part I, by using the hash strings to produce groups from adjacent blocks. It was good that I fixed my knot hash algorithm before getting to this Part, because I would have been completely off had I not. Anyway, after generating the hash strings, I convert all the 1's into #'s, so that the program can easily see which values need to be processed as a new group (those that didn't end up in other groups,yet.) Then I go through each of the rows in a scanning loop, starting with the first # it encounters and then recursively change the # into something else (I just used the group number, like the examples), and then check its neighbors to the right and left and above and below, using the same function. Once it doesn't find any other #'s as neighbors, it will return to the scanning loop to look for another # or group to work on. Since I'm using group numbers in place of the #'s, the group numbers are incremented at the beginning of each scan.

Note that strings are immutable in Python, so instead of having a large list of 128 rows of strings, I had to make 128 rows of lists, with each cell of that inner list only containing one character.
'''

puzzle_input = "amgozmfv"

# Test data!
# puzzle_input = "flqrgnkx"


def knot_hash(input_str):
    input_list = [ord(thisChar) for thisChar in input_str]
    input_list += [17, 31, 73, 47, 23]

    nums_list = [x for x in range(0, 256)]

    curr_pos = 0
    skip_size = 0

    for i in range(64):
        for this_range in input_list:
            # print("INPUT:", this_range, "CURSOR:", curr_pos, "SKIP:", skip_size, "NUMS_LIST:", nums_list)
            temp_list = []

            for j in range(curr_pos, curr_pos + this_range):
                nums_list_idx = j % len(nums_list)
                temp_list.append(nums_list[nums_list_idx])

            temp_list.reverse()

            for j in range(len(temp_list)):
                nums_list_idx = (curr_pos + j) % len(nums_list)
                nums_list[nums_list_idx] = temp_list[j]
            
            curr_pos = (curr_pos + this_range + skip_size) % len(nums_list)
            skip_size += 1
            # print("END LOOP - NUMS_LIST:", nums_list)
    # print("SPARSE HASH:", nums_list)

    dense_hash = []
    for i in range(16):
        total = 0
        for j in range(16):
            total ^= nums_list[(i*16) + j]
        dense_hash.append(total)
    # print("DENSE HASH:", dense_hash)

    final_hash = ""
    for this_num in dense_hash:
        final_hash += hex(this_num)[2:].zfill(2)
    
    return final_hash

# NEW: This is a recursive function, that takes a row, column, and a group number. The group number isn't really needed, but I use it because I wanted to replace the #'s with the common group numbers that are found adjacent to each other. It will check the given position to see if it's a #, and if it is not, it does not do anything. However, if it is a #, it will replace it with the group number and then check its neighbors, using another call to itself, with that position!
def processGroup(new_row, new_col, new_num):
    global all_rows  # Since we're changing this data structure.
    if all_rows[new_row][new_col] == "#":

        all_rows[new_row][new_col] = str(new_num)  # Replace the # with the group number.

        if (new_col + 1) < 128: processGroup(new_row, new_col + 1, new_num)  # Check to the right.
        if (new_col - 1) > -1: processGroup(new_row, new_col - 1, new_num)  # Check to the left.
        if (new_row + 1) < 128: processGroup(new_row + 1, new_col, new_num)  # Check to the top.
        if (new_row - 1) > -1: processGroup(new_row - 1, new_col, new_num)  # Check to the bottom.


all_rows = []  # NEW: Big data structure to contain all my binary string characters!
# Most of the follow loop is the same as from Part I -- just creating the hash strings.
for this_num in range(128):
    full_input = puzzle_input + "-" + str(this_num)
    this_hash = knot_hash(full_input)

    bin_str = bin(int(this_hash, 16))[2:].zfill(128)
    bin_str = bin_str.replace("1", "#")  # NEW: Converting 1's into #'s. Easier to see leftovers.
    all_rows.append(list(bin_str))  #  NEW: Turn string into list and add to the data structure.
    # print(bin_str)

# NEW: I had to process the lines in a separate loop (even though the number of loop iterations is the same) because I needed the data structure to exist before I could recursively traverse it in any direction.
group_num = 0  # Tracking what we're interested in at the end!
for this_row in range(128):
    while "#" in all_rows[this_row]:  # While there are leftover #'s in this line...
        group_num += 1  # Must be a new group to process!
        this_col = all_rows[this_row].index("#")  # Get the index of that #.
        # print("FOUND POTENTIAL GROUP AT: row:", this_row, "col:", this_col)
        processGroup(this_row, this_col, group_num)  # Recursive function, starting with that position!

# new_rows = ["".join(this_row) for this_row in all_rows]
# print("\n".join(new_rows))

print("TOTAL GROUPS:", group_num)
