# Advent of Code 2017
# Day 16 - Part II
# mushmine - Python


'''
I actually rewrote this one three times. The first time, I just wrapped everything in a for loop to 1000000000 for kicks, though I suspected the eventual outcome, given all the list manipulation and resizing: super long execution time. Like years. The second try, I changed everything to base it on a linked list structure, thinking maybe I could get away with just changing the "next" pointers. It was running significantly faster, but still not fast enough. I probably wouldn't get an answer until 2018 with it. So, I went back to the problem and then looked for patterns in behavior or output.

When looking for patterns in output, I realized that the output actually cycles back and repeats every 42 times! (Probably different for different problem inputs.) Knowing that, I just needed to divide by the number of times I was going to run it and if there was a remainder, only run the dance that number of times. However, to further optimize, since we're already tracking all the outputs per cycle, we don't have to run the dance anymore; the remainder can be used to determine which offset from the beginning of the cycle.
'''

with open("advent16.in", "r") as f: all_file_list = f.read().strip().split(",")
programs = list(map(chr, range(97, 97 + 16)))  # List instead of string, to support re-assignment!
num_dances = 1000000000  # NEW: A Billion?!! Holy cow.

# Test data!
# all_file_list = ["s1", "x3/4", "pe/b"]
# programs = list(map(chr, range(97, 97 + 5)))
# num_dances = 1

prev_progs = []  # NEW: To track the outcomes per dance cycle.
for i in range(num_dances):

    # NEW: Track previous outcomes and stop as soon as we see a repeat, assuming then that the cycle is complete!
    curr_progs = "".join(programs)  # Since our prev_progs is a list of strings, instead of list of lists. Simpler.
    if curr_progs in prev_progs:  # Have we seen this dance before?
        # print("CYCLE:", i, "PREVIOUS:", prev_progs)
        print("ANSWER:", prev_progs[num_dances % i])
        break
    else:
        prev_progs.append(curr_progs)  # If not, add it to the list of previous outputs!
    
    for this_move in all_file_list:
        if this_move[0] == "s":
            this_pos = int(this_move[1:])
            programs = programs[-this_pos:] + programs[:-this_pos]
        elif this_move[0] == "x":
            moves_list = this_move[1:].split("/")
            idx_1 = int(moves_list[0])
            idx_2 = int(moves_list[1])
            programs[idx_1], programs[idx_2] = programs[idx_2], programs[idx_1]
        elif this_move[0] == "p":
            moves_list = this_move[1:].split("/")
            idx_1 = programs.index(moves_list[0])
            idx_2 = programs.index(moves_list[1])
            programs[idx_1], programs[idx_2] = programs[idx_2], programs[idx_1]
    