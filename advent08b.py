# Advent of Code 2017
# Day 8 - Part I
# mushmine - Python


'''The second part is pretty easy, as we just need to check after each operation whether the last thing we just did produced a higher value than any other ever. We're using a variable to track the highest ever.'''

with open("advent08.in") as f:
    all_lines_list = f.readlines()  # Read from file as lines into a list of lines!

register = {}
highest_ever = 0  # NEW: Tracking variable!

for this_line in all_lines_list:
    tokens_list = this_line.strip().split(" ")

    target_expression = "register['" + tokens_list[0] + "']"
    if tokens_list[1] == 'inc': target_expression += " += "
    else: target_expression += " -= "
    target_expression += " " + tokens_list[2]

    condition = "register['" + tokens_list[4] + "'] " + " ".join(tokens_list[5:])

    if tokens_list[0] not in register: register[tokens_list[0]] = 0
    if tokens_list[4] not in register: register[tokens_list[4]] = 0

    new_statement = "if " + condition + ": " + target_expression
    # print("EVAL: " + new_statement)
    exec(new_statement)

    # NEW: Check to see if newly run instruction produced a highest ever value!
    if register[tokens_list[0]] > highest_ever: highest_ever = register[tokens_list[0]]

# print("REGISTER: ", register)
print("HIGHEST AT END: ", max(register.values()))
print("HIGHEST EVER: ", highest_ever)
