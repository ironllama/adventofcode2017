import math

with open("advent21a.txt", "r") as f: all_rules_list = f.readlines()
# all_rules_list = ["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"]

all_rules_dict = dict(this_line.split(" => ") for this_line in all_rules_list)

def rotate(matrix):
    numPerRow = len(matrix[0])
    newMatrix = [list(thisLine) for thisLine in matrix]  # Copy the original list
    for row in range(numPerRow):
        for col in range(numPerRow):
            newMatrix[row][col] = matrix[(numPerRow - 1) - col][row]
    return newMatrix

def flip(matrix):
    for row in range(len(matrix[0])):
        for col in range(int(len(matrix[0]) / 2)):
            matrix[row][col], matrix[row][(len(matrix) - 1) - col] = matrix[row][(len(matrix) - 1) - col], matrix[row][col]
    return matrix

def same(matrix_a, matrix_b):
    for row in range(len(matrix_a[0])):
        for col in range(len(matrix_a[0])):
            if matrix_a[row][col] != matrix_b[row][col]: return False
    return True

def getString(matrix):
    return "/".join(["".join(thisList) for thisList in matrix])

def getMatrix(matrix_str):
    return [list(this_row) for this_row in matrix_str.split("/")]

def checkDictionary(matrix_str):
    foundMatch = ""

    for j in range(4):
        # print("CHECK:", matrix_str)
        if matrix_str in all_rules_dict:
            foundMatch = all_rules_dict[matrix_str]
            break
        else:
            flip_matrix_str = getString(flip(getMatrix(matrix_str)))
            # print("CHECK2:", flip_matrix_str)
            if flip_matrix_str in all_rules_dict:
                foundMatch = all_rules_dict[flip_matrix_str]
                break
        matrix_str = getString(rotate(getMatrix(matrix_str)))

    if foundMatch == "": print("ERROR! NO MATCH!", matrix_str)
    return foundMatch.strip()

def get_new_matrix_str(matrix_obj, num):
    # print("get_new_matrix_str", matrix_obj)
    row_size = len(matrix_obj[0])  # Num of char per row.
    factor = int(row_size / num)  # How many groups of squares per row.
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


matrix_str = ".#./..#/###"

for i in range(5):
    matrix_obj = getMatrix(matrix_str)
    size = len(matrix_obj[0])
    if size % 2 == 0: matrix_str = get_new_matrix_str(matrix_obj, 2)
    elif size % 3 == 0: matrix_str = get_new_matrix_str(matrix_obj, 3)

print("STR:", matrix_str)
print("OBJ:\n" + "\n".join(["".join(this_list) for this_list in getMatrix(matrix_str)]))

num_hashes = 0
for i in matrix_str:
    if i == "#": num_hashes += 1
print("FINAL:", num_hashes)