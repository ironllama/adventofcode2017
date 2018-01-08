# Advent of Code 2017
# Day 7 - Part I
# mushmine - Python


'''This first one is pretty easy -- looking at the input, it seems that either a string token (disc name) can appear in the list with its weight and sub-towers, or it can be listed as a sub-tower in another's token line. So determining the root is simply to look for the token that's not every listed in any other token's sub-tower list. Or, collect all the possible sub-tower string tokens and remove the duplicates.'''

with open("advent07.in") as f:
    all_lines_list = f.readlines()  # Read from file as lines into a list of lines!

    # Test data!
    # all_lines_list = ["pbga (66)", "xhth (57)", "ebii (61)", "havc (66)", "ktlj (57)", "fwft (72) -> ktlj, cntj, xhth", "qoyq (66)", "padx (45) -> pbga, havc, qoyq", "tknk (41) -> ugml, padx, fwft", "jptl (61)", "ugml (68) -> gyxo, ebii, jptl", "gyxo (61)", "cntj (57)"]


root_token_buffer = []  # Just going to use this as a buffer of possible root tokens.

# Function that checks if the given token already exists in the root_token_buffer. If it does, it
# can not be a root, so it is removed. If it doesn't, it's added for further checking.
def process_token_for_root(in_token):
    if in_token in root_token_buffer:
        root_token_buffer.remove(in_token)
    else:
        root_token_buffer.append(in_token)

for this_line in all_lines_list:  # For each line in input.
    this_line = this_line.strip()  # Strip the newline at the end.
    new_token_name = this_line[0:this_line.index(" ")]  # Only get the string up to the first space.
    process_token_for_root(new_token_name)  # Send that token to be processed!

    if "->" in this_line:  # If the line also contains a list of sub-towers...
        sub_tokens_str = this_line[this_line.index("->") + 3:]  # Extract the list (string) from the line.
        sub_tokens_list = sub_tokens_str.split(", ")  # Create an actual list from the string.
        for this_subtoken in sub_tokens_list:  # Process each element in the list!
            process_token_for_root(this_subtoken)

print("ROOT:", root_token_buffer)
