# Advent of Code 2017
# Day 16 - Part I
# mushmine - Python


'''
The programs could have just been a string "abcdefghijklmnop", but I decided to have Python generate them. Didn't really save anything, but was a nice little mini-challenge. Other than that, it was pretty much reading each line of the file, chopping it up by spaces into tokens, the first being the code on which to make a move, and the rest determining the actors in the move.
'''

with open("advent16a.txt", "r") as f: all_file_list = f.read().strip().split(",")
programs = list(map(chr, range(97, 97 + 16))  # List instead of string, to support re-assignment!

# Test data!
# all_file_list = ["s1", "x3/4", "pe/b"]  # Test data!
# programs = list(map(chr, range(97, 97 + 5)))

for this_move in all_file_list:  # For each line in the file...
    move_code = this_move[0]  # The first character is the type of move.
    move_str = this_move[1:]  # The rest are the actor(s).
    if move_code == 's':
        this_pos = int(move_str)
        # beg_list = programs[:-this_pos]
        # end_list = programs[-this_pos:]
        # programs = end_list + beg_list
        programs = programs[-this_pos:] + programs[:-this_pos]  # This line is the combination of the previous 3 commented lines.
    if move_code == 'x':
        moves_list = this_move[1:].split("/")
        idx_1 = int(moves_list[0])
        idx_2 = int(moves_list[1])
        programs[idx_1], programs[idx_2] = programs[idx_2], programs[idx_1]  # Multiple assignment!
    if move_code == 'p':
        moves_list = this_move[1:].split("/")
        idx_1 = programs.index(moves_list[0])  # Same as move 'x', but get the index from the programs list.
        idx_2 = programs.index(moves_list[1])  # Same as move 'x', but get the index from the programs list.
        programs[idx_1], programs[idx_2] = programs[idx_2], programs[idx_1]  # Multiple assignment!

    # print(this_move, ":", programs)

print("FINAL:", "".join(programs))