# Advent of Code 2017
# Day 15 - Part I
# mushmine - Python


'''
This puzzle had a lot of reading, but if you follow the directions, it is not as difficult as the reading would suggest. Instead of having two concurrent generators running async, I just called a function twice with the different generator parameters as function arugments.
'''

pairs_found = 0  # To track the matches we find.
gen_a = 873  # Start value for generator A.
gen_b = 583  # Start value for generator B.

# Test values!
# gen_a = 65
# gen_b = 8921

# This is the logic of the generator, simply to multiply by a factor, and then get the remainder of division from a fixed number.
def generate_next(new_num, factor):
    new_num = new_num * factor
    new_num = new_num % 2147483647
    return new_num
    # return (new_num * factor) % 2147483647  # Single line, same as the lines above.

# Look for running the generator a fixed number of times.
# for this_num in range(5):  # Test data with 5 interations to match the instructions.
for this_num in range(40000000):
    gen_a = generate_next(gen_a, 16807)  # Run generator with the mutliplication factor per instructions.
    gen_b = generate_next(gen_b, 48271)  # Run generator with the mutliplication factor per instructions

    bit_a = bin(gen_a)[-16:]  # Turn in to bit string. Only interested in the last 16 digits.
    bit_b = bin(gen_b)[-16:]  # Turn in to bit string. Only interested in the last 16 digits.

    # print("GEN_A:", gen_a)
    # print("GEN_B:", gen_b)
    # print("BIT_A", bit_a)
    # print("BIT_B", bit_b)

    if bit_a == bit_b:  # If the stings match!
        pairs_found += 1
        # print(pairs_found, "MATCH!")

print("PAIRS FOUND:", pairs_found)