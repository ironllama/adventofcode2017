# Advent of Code 2017
# Day 10 - Part II
# mushmine - Python


'''While I commend AoC's efforts at teaching people how some hashing algorithms work, the nitty-gritty of coding one is not for the faint of heart! The good thing is that the instructions went through each step fairly well. Unfortunately, the complexity of trying to describe the operations even made me scratch my head a couple times. The difficulty in providing good examples each step of the way probably would make it that much more treacherous for those who lack confidence in their code.'''

input = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"  # Remember, your input could be different!

# Test values!
# input = ""
# input = "AoC 2017"
# input = "1,2,3"
# input = "1,2,4"

input_list = [ord(thisChar) for thisChar in input]  # NEW: Input converted into ASCII code equivalents. (Bytes!)
input_list += [17, 31, 73, 47, 23]  # NEW: Values added, per instructions.

nums_list = [x for x in range(0, 256)]

curr_pos = 0
skip_size = 0

for i in range(64):  # NEW: We're going to run our loop from the past exercise 64 times!
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
for i in range(16):  # There are 16 blocks of 16 numbers. This is to iterate over the 16 blocks.
    total = 0
    for j in range(16):  # Interate over the 16 numbers of each block.
        total ^= nums_list[(i*16) + j]  # Note the i*16 to skip past blocks. Also, XOR is associative, so we can do one at a time!
    dense_hash.append(total)  # Once a block is finished, add it to the list.

# print("DENSE HASH:", dense_hash)

final_hash = ""
for this_num in dense_hash:  # For each of the 16 numbers in the dense hash...
    # Covert into hex (we ignore the first two chars '/x'), make sure it's 2 digits long
    # and then concatenate to the string.
    final_hash += hex(this_num)[2:].zfill(2)

# print(nums_list)
print("KNOT HASH:", final_hash)