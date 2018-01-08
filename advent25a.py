# Advent of Code 2017
# Day 25 - Part I
# mushmine - Python


'''
It looked like there were some common things executed per state, so I figured I'd combine all the common actions into one function and only pass the things that the function needed to work -- things like what to write, which direction to move, and what the next state would be. I also used globals to track the state of the machine itself as it called this function more than 12 million times and used a list to track the stuff on the tape. (Thinking back on it, as I write this, I think that you could have also tracked the position of only the 1's in a set with a signed integers! Would have been more efficient. Next time.)
'''

state = "A"  # To track the current state of the machine.
cursor = 0  # To track the cursor as it moves back and forth on the tape.
tape = [0]  # To track the state of the tape.

# Function that accepts the different values, depending on what needs to be evaluated and manipulated.
def processPosition(current_value, zero_write, zero_move, zero_state, one_write, one_move, one_state):
    global state, cursor, tape  # Since we're changing the globals.

    if current_value == 0:
        tape[cursor] = zero_write  # Change the bit under the cursor.

        if zero_move == 1 and cursor == len(tape) - 1:  # If cursor is at end of list, but need to move right.
            tape.append(0)
            cursor += 1
        elif zero_move == -1 and cursor == 0:  # If cursort is at the start of list, but need to move left.
            tape.insert(0, 0)  # No need to change cursor, since list just shifted over.
        else:
            cursor += zero_move

        state = zero_state  # Change to new state!

    else:
        tape[cursor] = one_write  # Change the bit under the cursor.

        if one_move == 1 and cursor == len(tape) - 1:  # If cursor is at end of list, but need to move right.
            tape.append(0)
            cursor += 1
        elif one_move == -1 and cursor == 0:  # If cursort is at the start of list, but need to move left.
            tape.insert(0, 0)  # No need to change cursor, since list just shifted over.
        else:
            cursor += one_move

        state = one_state  # Change to new state!


# Test data, per example in text!
# for i in range(6):
#      current_value = int(tape[cursor])
#      if state == "A": processPosition(current_value, 1, 1, "B", 0, -1, "B")
#      elif state == "B": processPosition(current_value, 1, -1, "A", 1, 1, "A")

for i in range(12667664):
    current_value = int(tape[cursor])

    # All these per my puzzle input.
    if state == "A": processPosition(current_value, 1, 1, "B", 0, -1, "C")
    elif state == "B": processPosition(current_value, 1, -1, "A", 1, 1, "D")
    elif state == "C": processPosition(current_value, 0, -1, "B", 0, -1, "E")
    elif state == "D": processPosition(current_value, 1, 1, "A", 0, 1, "B")
    elif state == "E": processPosition(current_value, 1, -1, "F", 1, -1, "C")
    elif state == "F": processPosition(current_value, 1, 1, "D", 1, 1, "A")


# print("TAPE:", "".join(map(str, tape)))  # For testing and maybe secret message?
list_of_1s = [this_num for this_num in tape if this_num == 1]  # Count the number of 1's in the list.
print("CHECKSUM:", len(list_of_1s))