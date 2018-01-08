# Advent of Code 2017
# Day 18 - Part I
# mushmine - Python


'''
Parse through string instructions, one per line. Each instruction line is broken up into tokens, the first of which is the instruction itself that determines operation, the second is the register location to change, and the third (if applicable) is either a value to use in the operation, or a register location that has this value to use. Just looking for the first time a 'rcv' is called and the register location (second token) is not zero. The whole time, 'snd' operations set a variable (I called it last_freq), and at the end of the program, the last value that was assigned to that variable is displayed.
'''

with open("advent18a.txt", "r") as f: all_lines_list = f.readlines()

# Test data!
# all_lines_list = ["set a 1", "add a 2", "mul a a", "mod a 5", "snd a", "set a 0", "rcv a", "jgz a -1", "set a 1", "jgz a -2"]

curr_pos = 0  # Track current position while going through the loop.
last_freq = 0  # Track the last sound that was made.
registers = {}  # The registers!

while True:
    line_tokens = all_lines_list[curr_pos].strip().split(" ")  # Split line into string tokens. (instruction X Y)
    skip_num = 1  # Number of instructions to jump at the end of the loop interation.

    if line_tokens[1] not in registers: registers[line_tokens[1]] = 0  # If the X doesn't exist, make one.
    # print ("LOOP line_tokens:", line_tokens, "curr_pos:", curr_pos, "registers:", registers)

    if len(line_tokens) > 2 and line_tokens[2].isalpha():  # Sometimes Y is a letter, sometimes it's a value.
        line_tokens[2] = registers[line_tokens[2]]  # If letter, use it to get value at that register location.

    # Depending on instruction, maybe possible actions...
    if line_tokens[0] == "snd": last_freq = registers[line_tokens[1]]  # Store the sound!
    elif line_tokens[0] == "set": registers[line_tokens[1]] = int(line_tokens[2])
    elif line_tokens[0] == "add": registers[line_tokens[1]] += int(line_tokens[2])
    elif line_tokens[0] == "mul": registers[line_tokens[1]] *= int(line_tokens[2])
    elif line_tokens[0] == "mod": registers[line_tokens[1]] %= int(line_tokens[2])
    elif line_tokens[0] == "rcv":
        if registers[line_tokens[1]] != 0:  # Looking for first non-zero recover instruction!
            # print("RECOVERY! line_tokens:", line_tokens, "LAST_FREQ:", last_freq)
            break
    elif line_tokens[0] == "jgz":
        if registers[line_tokens[1]] > 0: skip_num = int(line_tokens[2])  # Number of instructions to jump.
    
    curr_pos += skip_num  # Go to the next instruction.
    if curr_pos < 0 or curr_pos > len(all_lines_list): break  # If instructions jump out of register, exit.

print("LAST_FREQ:", last_freq)