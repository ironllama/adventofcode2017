# Advent of Code 2017
# Day 23 - Part I
# mushmine - Python


'''
Parse through string instructions, one per line. Each instruction line is broken up into tokens, the first of which is the instruction itself that determines operation, the second is the register location to change, and the third (if applicable) is either a value to use in the operation, or a register location that has this value to use. Use a variable to track the number of times the 'mul' instruction is used.
'''

with open("advent23a.txt", "r") as f: all_lines_list = f.readlines()

curr_pos = 0  # Track current position while going through the loop.
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0,'e': 0, 'f': 0, 'g': 0, 'h': 0}  # The registers!

num_mul = 0  # Track number of times mul is done.
while True:
    line_tokens = all_lines_list[curr_pos].strip().split(" ")  # Split line into string tokens. (instruction X Y)
    skip_num = 1  # Number of instructions to jump at the end of the loop interation.

    if line_tokens[2].isalpha():  # Sometimes Y is a letter, sometimes it's a value.
        line_tokens[2] = registers[line_tokens[2]]  # If a letter, get the value at that register location.

    # Depending on instruction, maybe possible actions...
    if line_tokens[0] == "set": registers[line_tokens[1]] = int(line_tokens[2])
    elif line_tokens[0] == "sub": registers[line_tokens[1]] -= int(line_tokens[2])
    elif line_tokens[0] == "add": registers[line_tokens[1]] += int(line_tokens[2])
    elif line_tokens[0] == "mul":
        registers[line_tokens[1]] *= int(line_tokens[2])
        num_mul += 1
    elif line_tokens[0] == "jnz":
        if line_tokens[1].isalpha():  # Sometimes X is a letter, sometimes it's a value.
            line_tokens[1] = registers[line_tokens[1]]  # If letter, get the value at that register location.

        if int(line_tokens[1]) != 0: skip_num = int(line_tokens[2])  # instructions to jump.

    # print ("LOOP line_tokens:", line_tokens, "curr_pos:", curr_pos, "registers:", registers)
    
    curr_pos += skip_num  # Go to the next instruction.
    if curr_pos < 0 or curr_pos >= len(all_lines_list): break  # If instructions out of register, exit.

print("NUMBER OF MULS:", num_mul)