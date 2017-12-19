# Advent of Code 2017
# Day 18 - Part II
# mushmine - Python


'''
Two parallel programs.
'''

with open("advent18a.txt", "r") as f: all_lines_list = f.readlines()

# Test data!
# all_lines_list = ["set a 1", "add a 2", "mul a a", "mod a 5", "snd a", "set a 0", "rcv a", "jgz a -1", "set a 1", "jgz a -2"]
# all_lines_list = ["snd 1", "snd 2", "snd p", "rcv a", "rcv b", "rcv c", "rcv d"]

curr_pos_0 = 0
registers_0 = {'p': 0}
input_0 = []

curr_pos_1 = 0
registers_1 = {'p': 1}
input_1 = []

num_sends_by_1 = 0
def processLine(in_registers, in_pos, in_input, in_id):
    while True:
        global num_sends_by_1

        line_tokens = all_lines_list[in_pos].strip().split(" ")  # Split the instruction line into string tokens. (instruction X Y)
        skip_num = 1  # Number of instructions to jump at the end of the loop interation.

        if line_tokens[1] not in in_registers: in_registers[line_tokens[1]] = 0  # If the X doesn't exist, make one.
        # print ("LOOP line_tokens:", line_tokens, "in_pos:", in_pos, "in_registers:", in_registers)

        if len(line_tokens) > 2 and line_tokens[2].isalpha():  # Sometimes the Y is an index letter, sometimes it's a value.
            line_tokens[2] = in_registers[line_tokens[2]]  # If it's a letter, use it to get the value at that register location.

        # Depending on instruction, maybe possible actions...
        if line_tokens[0] == "snd":
            if line_tokens[1].isalpha():  # Sometimes the Y is an index letter, sometimes it's a value.
                line_tokens[1] = in_registers[line_tokens[1]]  # If it's a letter, use it to get the value at that register location.
            if in_id == 0:
                input_1.append(int(line_tokens[1]))
                # print("ADDING TO 1:", len(input_1))
            else:
                input_0.append(int(line_tokens[1]))
                num_sends_by_1 += 1
                # print("ADDING TO 0:", len(input_0))
        elif line_tokens[0] == "set": in_registers[line_tokens[1]] = int(line_tokens[2])
        elif line_tokens[0] == "add": in_registers[line_tokens[1]] += int(line_tokens[2])
        elif line_tokens[0] == "mul": in_registers[line_tokens[1]] *= int(line_tokens[2])
        elif line_tokens[0] == "mod":
            if int(line_tokens[2]) != 0: in_registers[line_tokens[1]] %= int(line_tokens[2])
            else: in_registers[line_tokens[1]] = 0
        elif line_tokens[0] == "rcv":
            if len(in_input) > 0:
                in_registers[line_tokens[1]] = in_input.pop(0)
                # print("POPPING:", len(in_input))
            else: return in_pos
        elif line_tokens[0] == "jgz":
            if in_registers[line_tokens[1]] > 0: skip_num = int(line_tokens[2])  # Change the number of instructions to jump.
        
        in_pos += skip_num  # Go to the next instruction.
        if in_pos < 0 or in_pos > len(all_lines_list): break  # If the instructions take it out of the register, exit.

while True:
    curr_pos_0 = processLine(registers_0, curr_pos_0, input_0, 0)
    # print("CURR_0:", curr_pos_0, "INPUT_0:", input_0, "CURR_1:", curr_pos_1, "INPUT_1:", input_1)
    print("INPUT_1:", input_1)
    curr_pos_1 = processLine(registers_1, curr_pos_1, input_1, 1)
    # print("CURR_0:", curr_pos_0, "INPUT_0:", input_0, "CURR_1:", curr_pos_1, "INPUT_1:", input_1)
    print("INPUT_0:", input_0)
    if len(input_0) == 0 and len(input_1) == 0: break


print("VALUES SENT BY PROGRAM 1:", num_sends_by_1)