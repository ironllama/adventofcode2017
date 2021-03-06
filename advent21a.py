# Advent of Code 2017
# Day 21 - Part I
# mushmine - Python


'''
Day 21 was more of a conceptual pain than a programming pain. To help me get through some of the complexity, I decided to split out the different things that needed to be done per step (rotate, flip, compare, etc.)

This lets me simplify the logic and steps that need to be taken to determine further actions. Also let me handle the complexity by doing it in small pieces.
'''

with open("advent21.in", "r") as f: all_rules_list = f.readlines()
# all_rules_list = ["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"]  # Test data!

all_rules_dict = dict(this_line.split(" => ") for this_line in all_rules_list)  # Process lines into dictionary.

# Rotates an arbitrarily sized matrix, by moving [row][col] into [col][row] with some maths.
def rotate(matrix):
    numPerRow = len(matrix[0])
    newMatrix = [list(thisLine) for thisLine in matrix]  # Copy the original list
    for row in range(numPerRow):
        for col in range(numPerRow):
            newMatrix[row][col] = matrix[(numPerRow - 1) - col][row]
    return newMatrix

# Flips an arbitrarily sized matrix, by moving first in row to last and collapsing towards the center.
def flip(matrix):
    for row in range(len(matrix[0])):
        for col in range(int(len(matrix[0]) / 2)):
            matrix[row][col], matrix[row][(len(matrix) - 1) - col] = matrix[row][(len(matrix) - 1) - col], matrix[row][col]
    return matrix

# Compares two matrices to see if they are the same. Short-circuit returns false if it finds a difference.
def same(matrix_a, matrix_b):
    for row in range(len(matrix_a[0])):
        for col in range(len(matrix_a[0])):
            if matrix_a[row][col] != matrix_b[row][col]: return False
    return True

# Convenience function to turn a matrix into a string. (Like in the input.)
def getString(matrix):
    return "/".join(["".join(thisList) for thisList in matrix])

# Convenience to turn a string into a matrix (multi-dimensional list).
def getMatrix(matrix_str):
    return [list(this_row) for this_row in matrix_str.split("/")]

# Checks to see if the given string (matrix_str) exists in the Dictionary (input list).
# This could probably be optimized, since there might be overlap in combos of rotate/flip?
def checkDictionary(matrix_str):
    foundMatch = ""

    for j in range(4):  # 4 for each 90deg rotation of the matrix.
        # print("CHECK:", matrix_str)
        if matrix_str in all_rules_dict:
            foundMatch = all_rules_dict[matrix_str]
            break
        else:
            # If it doesn't exist as it is, currently, flip it and check again.
            flip_matrix_str = getString(flip(getMatrix(matrix_str)))
            # print("CHECK2:", flip_matrix_str)
            if flip_matrix_str in all_rules_dict:
                foundMatch = all_rules_dict[flip_matrix_str]
                break
        matrix_str = getString(rotate(getMatrix(matrix_str)))  # If still no match, rotate and try again!

    if foundMatch == "": print("ERROR! NO MATCH!", matrix_str)  # Hopefully, never see this!
    return foundMatch.strip()  # Return the cooresponding pattern from Dictionary.

# Function to split a large matrix (matrix_obj) into smaller matrices, by factor of a given number (num).
# Then, finds the replacement string in the Dictionary and grow out to the necessary size.
def get_new_matrix_str(matrix_obj, num):
    # print("get_new_matrix_str", matrix_obj)
    row_size = len(matrix_obj[0])  # Num of char per row.
    factor = int(row_size / num)  # How many groups of squares per row.

    # First, do the split into smaller matrices and check against dictionary to get replacements.
    new_matrix_str = ""
    for x in range(factor):
        for y in range(factor):
            this_matrix_str = ""
            for row in range(num):
                for col in range(num):
                    # print("GETTING:", row_size, factor, x, y, row, col)
                    this_matrix_str += matrix_obj[(num * x) + row][(num * y) + col]
                this_matrix_str += "/"
            this_matrix_str = this_matrix_str.strip("/")
            new_matrix_str += checkDictionary(this_matrix_str) + "/"
    new_matrix_str = new_matrix_str.strip("/")

    # Now grow the matrix accordingly, based on the string replacements.
    # print("REPLACEMENT:", new_matrix_str)
    new_matrix_list = new_matrix_str.split("/")
    new_matrix_str = ""
    for row in range(factor):
        for x in range(len(new_matrix_list[0])):
            for col in range(factor):
                # print("LOOP:", factor, row, col, x)
                new_matrix_str += new_matrix_list[(row * int(len(new_matrix_list) / factor)) + (col * len(new_matrix_list[0])) + x]
            new_matrix_str += "/"
    new_matrix_str = new_matrix_str.strip("/")

    # print("HERE:", new_matrix_str)
    return new_matrix_str


matrix_str = ".#./..#/###"  # Starting matrix.

for i in range(5):
    matrix_obj = getMatrix(matrix_str)  # Turn the matrix string into an object.
    size = len(matrix_obj[0])

    # Grow the matrix, accordingly.
    if size % 2 == 0: matrix_str = get_new_matrix_str(matrix_obj, 2)
    elif size % 3 == 0: matrix_str = get_new_matrix_str(matrix_obj, 3)

# print("STR:", matrix_str)
# print("OBJ:\n" + "\n".join(["".join(this_list) for this_list in getMatrix(matrix_str)]))

# Count the number of hashes in the final matrix, by just interating through the final string.
num_hashes = 0
for i in matrix_str:
    if i == "#": num_hashes += 1

print("FINAL:", num_hashes)