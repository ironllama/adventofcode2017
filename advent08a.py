# Advent of Code 2017
# Day 8 - Part I
# mushmine - Python


'''This one is also linear - literally: you process one line at a time. One could parse each string by separating out into tokens, and then depending on the value of the token, branch out into if/else/switch branches to execute different tasks. I noticed that the conditional part of each instruction line was pretty similiar in syntax to what Python uses (!=, ==, etc.) so I wanted to use eval() or exec() to run them. While I would almost never do this in actual customer production code, this is just for fun, so I ended up using exec(). (The eval() can only do simple expressions, so the if statement makes it barf.) So the challenge was just string parsing into a correct and executable Python string.'''

with open("advent08a.txt") as f:
    all_lines_list = f.readlines()  # Read from file as lines into a list of lines!

register = {}  # Where I store all my values.

for this_line in all_lines_list:
    tokens_list = this_line.strip().split(" ")  # Clean up string and cut up into tokens/words.

    # Start building string to execute -- using my register list! Just need to translate 'inc' into ' += ' and 'desc' into ' -= '.
    target_expression = "register['" + tokens_list[0] + "']"
    if tokens_list[1] == 'inc': target_expression += " += "
    else: target_expression += " -= "
    target_expression += " " + tokens_list[2]

    # Build up the if condition for my string.
    condition = "register['" + tokens_list[4] + "'] " + " ".join(tokens_list[5:])

    # If the register locations don't yet exist, create them with 0 as value.
    if tokens_list[0] not in register: register[tokens_list[0]] = 0
    if tokens_list[4] not in register: register[tokens_list[4]] = 0

    # Final construction of the string to run!
    new_statement = "if " + condition + ": " + target_expression
    # print("EVAL: " + new_statement)
    exec(new_statement)  # Run it! String -> Python code!

# print("REGISTER: ", register)
# Now, just extract the highest value found in the dictionary.
print("HIGHEST: ", max(register.values()))
