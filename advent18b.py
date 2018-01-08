# Advent of Code 2017
# Day 18 - Part II
# mushmine - Python


'''
Two parallel programs. Added an 'incoming' list queue for both programs and separate tracking on where they were in the program with separate variables. Also, of course, different starting values for p.

Essentially, run the first program until it exhausted the incoming queue and needed more values from the other program, then kicked off the other program and ran that the same way, exhausting its incoming queue until it waits for the other program, and so on.

This took me an inordinate time to figure out because of a small bug, that I want to blame on the unclear instructions. It seemed that the only command that MAY have a integer as X was the jgz command. Without addressing this possibility, the two programs send ever larger messages to each other and never end up stopping. This wasn't really addressed in the instructions or examples, and it was only spotted after it sat untouched for a couple weeks and I looked through it again, with fresh eyes. So, I guess some of the blame is one me, the programmer for not vetting the input. Anyway, after fixing the bug, it produced the answer immediately.
'''

with open("advent18a.txt", "r") as f: all_lines_list = f.readlines()

# Test data!
# all_lines_list = ["set a 1", "add a 2", "mul a a", "mod a 5", "snd a", "set a 0", "rcv a", "jgz a -1", "set a 1", "jgz a -2"]
# all_lines_list = ["snd 1", "snd 2", "snd p", "rcv a", "rcv b", "rcv c", "rcv d"]

curr_pos_0 = 0  # NEW: Track the current instruction for program 0.
registers_0 = {'p': 0} # NEW: Registers for program 0.
input_0 = []  # Track stuff for program 0 to process.

curr_pos_1 = 0  # NEW: Track the current instruction for program 1.
registers_1 = {'p': 1} # NEW: Registers for program 1.
input_1 = []  # Track stuff for program 1 to process.

num_sends_by_1 = 0  # Track the answer for the puzzle -- number of sends by program 1!

# NEW: The processing was put into a function so it could be alternately called for each program.
# Most of the content of the function is the same as from Part I.
def processLine(in_registers, in_pos, in_input, in_id, in_output):
    while True:
        global num_sends_by_1  # NEW: We're changing this global variable.

        line_tokens = all_lines_list[in_pos].strip().split(" ")
        skip_num = 1

        if line_tokens[1] not in in_registers: in_registers[line_tokens[1]] = 0

        if len(line_tokens) > 2 and line_tokens[2].isalpha():
            line_tokens[2] = in_registers[line_tokens[2]]

        # Depending on instruction, maybe possible actions...
        if line_tokens[0] == "snd":
            # NEW: Add the value to the input queue of the other program!
            in_output.append(int(in_registers[line_tokens[1]]))
            if in_id == 1: num_sends_by_1 += 1
        elif line_tokens[0] == "set": in_registers[line_tokens[1]] = int(line_tokens[2])
        elif line_tokens[0] == "add": in_registers[line_tokens[1]] += int(line_tokens[2])
        elif line_tokens[0] == "mul": in_registers[line_tokens[1]] *= int(line_tokens[2])
        elif line_tokens[0] == "mod":
            # NEW: Sometimes the value to mod is 0, which produces an error, and needs to be handled.
            if int(line_tokens[2]) != 0: in_registers[line_tokens[1]] %= int(line_tokens[2])
            else: in_registers[line_tokens[1]] = 0
        elif line_tokens[0] == "rcv":
            # NEW: Either read the data from the input queue (if exists), or go back to run the other program.
            if len(in_input) > 0: in_registers[line_tokens[1]] = in_input.pop(0)
            else: return in_pos
        elif line_tokens[0] == "jgz":
            if line_tokens[1].isalpha():  # Since X MAY or may not be a number.
                line_tokens[1] = in_registers[line_tokens[1]]
            if int(line_tokens[1]) > 0: skip_num = int(line_tokens[2])  # Number of instructions to jump.
        
        in_pos += skip_num
        if in_pos < 0 or in_pos > len(all_lines_list): break

while True:
    curr_pos_0 = processLine(registers_0, curr_pos_0, input_0, 0, input_1)
    # print("CURR_0:", curr_pos_0, "INPUT_0:", input_0, "CURR_1:", curr_pos_1, "INPUT_1:", input_1)
    # print("A: INPUT_0:", len(input_0), "INPUT_1:", len(input_1))
    if len(input_1) == 0: break
    curr_pos_1 = processLine(registers_1, curr_pos_1, input_1, 1, input_0)
    # print("CURR_0:", curr_pos_0, "INPUT_0:", input_0, "CURR_1:", curr_pos_1, "INPUT_1:", input_1)
    # print("B: INPUT_0:", len(input_0), "INPUT_1:", len(input_1))
    if len(input_0) == 0: break


print("VALUES SENT BY PROGRAM 1:", num_sends_by_1)