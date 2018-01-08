# Advent of Code 2017
# Day 7 - Part II
# mushmine - Python


'''The second part is a bit maddening. It seems you'll have to use recursion to traverse the relationships, while making sure the sub-tower totals match up. Using recursion, one could get to the string tokens (discs) that have no sub-towers and then add-up as one unrolls the recursion, looking for inconsistencies in totals per branch level as one unrolls.

I combined this with Part I, to generate the root "branch" and start the recursive walk.'''

with open("advent07.in") as f:
    all_lines_list = f.readlines()  # Read from file as lines into a list of lines!
    # all_lines_list = ["pbga (66)", "xhth (57)", "ebii (61)", "havc (66)", "ktlj (57)", "fwft (72) -> ktlj, cntj, xhth", "qoyq (66)", "padx (45) -> pbga, havc, qoyq", "tknk (41) -> ugml, padx, fwft", "jptl (61)", "ugml (68) -> gyxo, ebii, jptl", "gyxo (61)", "cntj (57)"]


root_token_buffer = []
all_weights = {}  # NEW: To track all the weights, using the token name for direct access.
all_subtowers = {}  # NEW: To track all sub-towers, indexed by token name, as well.

def process_token_for_root(in_token):
    if in_token in root_token_buffer:
        root_token_buffer.remove(in_token)
    else:
        root_token_buffer.append(in_token)

for this_line in all_lines_list:
    this_line = this_line.strip()
    new_token_name = this_line[0:this_line.index(" ")]
    process_token_for_root(new_token_name)

    # NEW: Extract the weight from the line and add to the all_weights dictionary, stored number the name.
    new_token_weight = this_line[this_line.index("(") + 1:this_line.index(")")]
    all_weights[new_token_name] = int(new_token_weight)

    if "->" in this_line:
        sub_tokens_str = this_line[this_line.index("->") + 3:]
        sub_tokens_list = sub_tokens_str.split(", ")
        for this_subtoken in sub_tokens_list:
            process_token_for_root(this_subtoken)
        all_subtowers[new_token_name] = sub_tokens_list  # NEW: Store the sub-tokens in the dictionary!

print("ROOT:", root_token_buffer)

# NEW: This is the recursive function that is called, starting from the root, and building up the call stack as it traverses deeper into the tree. I don't like that it chews up memory this way, but the data shouldn't be big enough to cause any problems.
def get_weight_subbranch(in_branch):
    # print("get_weight_subbranch(", in_branch, ")")

    if in_branch in all_subtowers:  # If this branch (disc) has sub-branches (or leaves).
        all_branches = all_subtowers[in_branch]  # Get all the sub-towers for this branch (disc).

        branch_weights = []  # Track all possible weights to figure out which, if any, is different.

        # For all possible sub-branches, add up the branch weight, and all its sub-branch weights. Using recursion for the sub-branches.
        for this_branch in all_branches:  # Could have be done with a long list comprehension
            branch_weights.append(all_weights[this_branch] + get_weight_subbranch(this_branch))

        for i, this_weight in enumerate(branch_weights):  # Could also use for loop with interator.
            # For each weight possibility, this will extract any other weights that are the same.
            num_weights = [val for val in branch_weights if val == this_weight]

            if len(num_weights) == 1: # If there a unique weight in the list, we found our problem.
                # print("ALL_WEIGHTS", branch_weights)
                problem_weight = num_weights[0]
                problem_branch = all_branches[i]
                print("PROBLEM WITH", problem_branch, ": ", problem_weight, "OTHERS:", branch_weights)

                # Remove the problem weight and the rest of the list should be good weights!
                branch_weights.remove(problem_weight)
                common_weights = branch_weights[0]  # Using the first, assuming they are the same.
                print("LISTED WEIGHT:", all_weights[problem_branch], "-- SHOULD BE:", all_weights[problem_branch] - abs(common_weights - problem_weight))
                exit() #  No need to keep going.

        # Sub-branches will have to added up to be added to their parent branches, so let's total!
        total = branch_weights[0] * len(all_branches)  # Using the first, assuming they are the same.
        # print ("GOOD! BRANCHES:", len(all_branches), "EACH:", branch_weights[0], "TOTAL:", total)
        return total  # Pass the total weight of this child branch back to the parent for adding.

    else:
        return 0  # If there are no sub-branches (this is a leaf), then the sub-branch weight is 0.

get_weight_subbranch(root_token_buffer[0])
