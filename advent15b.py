# Advent of Code 2017
# Day 15 - Part II
# mushmine - Python


'''
This part changes the generating of the numbers, by having them only be certain multiples. While slowing things down, the loop is 8x smaller, so it should somewhat compensate? The rest is pretty much the same.
'''

pairs_found = 0
gen_a = 873
gen_b = 583

# Test values!
# gen_a = 65
# gen_b = 8921

# NEW: Changed this function so that I also accepts a parameter called multiple that will be used to determine when to stop generating new numbers (evenly divisible by the multiple) and returns that number.
def generate_next(new_num, factor, multiple):
    while True:
        new_num = (new_num * factor) % 2147483647  # Same as original function!
        if new_num % multiple == 0: break
    return new_num

# for this_num in range(5):
for this_num in range(5000000):
    gen_a = generate_next(gen_a, 16807, 4)  # NEW: Added multiple as last parameter.
    gen_b = generate_next(gen_b, 48271, 8)  # NEW: Added multiple as last parameter.

    bit_a = bin(gen_a)[-16:]
    bit_b = bin(gen_b)[-16:]

    # print("GEN_A:", gen_a)
    # print("GEN_B:", gen_b)
    # print("BIT_A", bit_a)
    # print("BIT_B", bit_b)

    if bit_a == bit_b:
        pairs_found += 1
        # print(pairs_found, "MATCH!")
    
print("PAIRS FOUND:", pairs_found)