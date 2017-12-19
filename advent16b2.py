
with open("advent16a.txt", "r") as f: all_file_list = f.read().strip().split(",")
programs = list(map(chr, range(97, 97 + 16)))  # List instead of string, to support re-assignment!
num_dances = 1000000000  # NEW: A Billion?!! Holy cow.

# Test data!
# all_file_list = ["s1", "x3/4", "pe/b"]
# programs = list(map(chr, range(97, 97 + 5)))
# num_dances = 1

# Pre-process all the instructions in a list, so we don't have to reprocess strings per loop.
for i in range(len(all_file_list)):
    move_code = all_file_list[i][0]
    move_str = all_file_list[i][1:]

    if move_code == "s": moves_list = [int(move_str)]
    else:
        moves_list = move_str.split("/")
        if move_code == "x":
            moves_list = [int(this_num) for this_num in moves_list]
            # if moves_list[0] > moves_list[1]: moves_list[0], moves_list[1] = moves_list[1], moves_list[0]
    all_file_list[i] = [move_code, moves_list]


class AlphaNode:
    def __init__(self, new_num, new_next):
        self.char = str(chr(new_num))
        self.next = new_next

def get_nodes():
    this_node = root_node
    final_str = ""
    while this_node != None:
        final_str += this_node.char
        this_node = this_node.next
    return final_str


num_chars = len(programs)
root_node = None
last_node = None
for i in range(97, 97 + num_chars):
    new_node = AlphaNode(i, None) 

    if root_node != None: last_node.next = new_node
    else: root_node = new_node

    last_node = new_node

print("START:", get_nodes())

for this_dance in range (1000000000):
# for this_dance in range (1):
    for this_move in all_file_list:
        move_code = this_move[0]
        move_list = this_move[1]

        if move_code == 's':
            idx_start = int(num_chars - move_list[0])
            this_node = root_node

            for i in range(idx_start - 1): this_node = this_node.next
            start_node = this_node.next
            this_node.next = None

            this_node = start_node
            while this_node.next != None: this_node = this_node.next
            this_node.next = root_node

            root_node = start_node

        elif move_code == "x":
            this_node = root_node
            for i in range(move_list[0]): this_node = this_node.next
            node_1 = this_node

            for i in range(move_list[1] - move_list[0]): this_node = this_node.next
            node_2 = this_node

            node_1.char, node_2.char = node_2.char, node_1.char

        elif move_code == "p":
            char_1 = move_list[0]  # Store for later assignment.
            char_2 = move_list[1]
            this_node = root_node
            num_found = 0
            while num_found < 2:
                if this_node.char == char_1 or this_node.char == char_2:
                    if this_node.char == char_1: this_node.char = char_2
                    else: this_node.char = char_1
                    num_found += 1
                this_node = this_node.next

        # print(this_move, ":", get_nodes())
    if this_dance % 10 == 0: print(this_dance + 1, ":", get_nodes())  # Get an idea of rate of execution.

print("FINAL:", get_nodes())