# Advent of Code 2017
# Day 14 - Part I
# mushmine - Python


'''
This puzzle reuses some code from a previous puzzle, so I just copied and pasted that code into this one, and then packaged that code into a function called knot_hash() for easy use. I could have also just put the function into a separate file and imported it, but then I have external dependencies and I want to keep each of these puzzle files separate. (Which is also why I also keep a separate Part I and II file for each Day, even though they share a lot of the same code.)

Anyway, today's puzzle is essentially to use the "knot hash" algorithm from Day 10 with a given puzzle input and a basic nonce (arbitrary number that changes and is only used once to create a hash) to generate the knot hash. Then to convert that hash (hex string), we convert it into a binary bit string (with some leading 0's, if needed), and then count the 1's!

NOTE: I realized when comparing the output of the hash in the example to my output, that there were some differences. While my answer worked, it seemed that I was missing something. The fact that my answer had worked suggested to me that I had some 0 padding issues. So, I printed out my hashes, and sure enough, I found that some of my hashes short of the full length that was expected because of hex values that were not 0 padded. For example, 0x7 was supposed to be '07', but I was outputing '7'. I fixed the knot hash algorithm from Day 10 and reran today's solution, and sure enough, the same final answer. However, now my string hash diagram using the test data matched the one in the example.
'''

puzzle_input = "amgozmfv"

# Test data!
# puzzle_input = "flqrgnkx"

# Taken from Day 10! Pretty much copy/paste, but minor variable name tweaks to put it in a function.
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
        final_hash += hex(this_num)[2:].zfill(2)  # NEW: FIX -- Left 0 padding on hex values.
    
    return final_hash


total_blocks = 0  # Tracking what is interesting!
for this_num in range(128):  # For nonces 0-127
    full_input = puzzle_input + "-" + str(this_num)  # Generate the string to use with knot hashing.
    # print("PROCESSING:", full_input)
    this_hash = knot_hash(full_input)  # Run the knot hash!
    # print("HASH:", this_hash)  # How I found the problem.

    bin_int = int(this_hash, 16)  # First, converting the knot hash into an int.
    bin_str = bin(bin_int)[2:]  # Then convert into biinary string, without the leading '0b'.
    bin_str = bin_str.zfill(128)  # Pad the left with 0's.
    # bin_str = bin(int(this_hash, 16))[2:].zfill(128)  # Same as above, all in one line!
    # print(bin_str)
    num_blocks = bin_str.count("1")  # Just need to count blocks, or 1's.
    total_blocks += num_blocks  # Add up with past values!


print("TOTAL BLOCKS:", total_blocks)
