# Advent of Code 2017
# Day 13 - Part II
# mushmine - Python


'''I wish I could say I found a prettier way of doing this, but I just did it the easy, inefficient way -- brute force! I tried every picosecond combination until I found one that yielded no catches!'''


with open("advent13a.txt", "r") as f:
    all_file_list = f.readlines()

    # Test data!
    # all_file_list = ["0: 3", "1: 2", "4: 4", "6: 4"]

delay = -1  # NEW: Starting delay at -1, since the loop starts by incrementing delay

while True:  # Keep trying! There will be breaks in the loop when we find what we're looking for.
    got_caught = False  # To see if we can break out early!
    delay += 1  #  Delay increment to test next delay value.

    for this_line in all_file_list:
        this_line_list = this_line.split(": ", 1)
        depth = int(this_line_list[0])
        range = int(this_line_list[1])

        range_cycle = (range * 2) - 2
        sweep_pos = (depth + delay) % range_cycle  # NEW: Added the delay to the calculation.

        if sweep_pos == 0:
            # NEW: Only need to see if we get caught, if we do, break out early and try the next delay.
            got_caught = True
            break
    
    if not got_caught: break  # If we made it completely past, break out of while loop. We're finished!

print("DELAY NEEDED:", delay)
