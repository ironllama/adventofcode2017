# Advent of Code 2017
# Day 13 - Part I
# mushmine - Python


'''A good part of this problem was spent figuring out what they wanted and then trying to find the proper pattern to use. I thought about looking up a formula or approach for the sweeping mechanism (versus the standard wrapping mechanism), but then found the challenge too fun to spoil with Google. And in turn, it was that much more rewarding when it was finally put together and used!

Each level has a number of cells it can sweep over, and the number of steps it takes per full sweep or full range cycle (back to the starting point) is pretty much double, since each cell gets hit on the first sweep out and then again on the sweep back, except for the first and the last cells, which only get hit once: at the beginning and at the end of each swing. For example, if a level has a range of 5 cells to sweep over, the pattern of cell numbers it will hit in turn looks like: 0 1 2 3 4 3 2 1. This will repeat again with the next full sweep cycle. So the full range cycle can be described as (range * 2) - 2.

From here, for the first half of the range (in the previous example, 0 1 2 3) as a modulo to the full range cycle, or depth % range_cycle, since the cycle keeps repeating over and over again. At this point, we know a packet will hit the scanner if this modulo is 0 -- the top of the scan cycle.

If you want to go one step further, you can get the exact position of the sweep. While not needed for this puzzle, here it is for my own curiosity. The second cell of the 2nd sweep is the same as the second cell of the 15th sweep, is the same as the second cell of the 187th sweep. However, the modulo only works until it hits the last half of the range cycle, because the numbers have to come back down, instead of going up. In other words, we would be finished if the numbers were: 0 1 2 3 4 5 6 7. But since the last three are actually 3 2 1, instead of 5 6 7, we have to adjust the math. Each is a shrinking amount from the end of the full cycle range, like -3 -2 -1, so we can describe it as range_cycle - (depth % range_cycle).

For this puzzle, the depth and time are the same, since the packet only goes one depth per picosecond. At 0 picoseconds, it's at the 0 depth. At 1 picoseconds, it's at depth 1. At 5 picoseconds it's at depth 5. And at 98 picoseconds, it's at depth 98. Depth and time are the same!'''

with open("advent13.in", "r") as f:
    all_file_list = f.readlines()

    # Test data!
    # all_file_list = ["0: 3", "1: 2", "4: 4", "6: 4"]

severity = 0  # Tracking variable for severity level -- we're going to add to this!
for this_line in all_file_list:  # For each string line...
    this_line_list = this_line.split(": ", 1)  # First split by the colon and space.
    depth = int(this_line_list[0])  # The left number will be the depth (or time).
    range = int(this_line_list[1])  # The second number is the range, or number of cells in the depth.

    range_cycle = (range * 2) - 2  # Number of cells in a full range sweep cycle.
    pos = depth % range_cycle  # Position is the modulo of the full range sweep cycle.
    # if pos > range: pos = range_cycle - pos  # Exact pos. If past half, it sweeps back down.

    if pos == 0: severity += depth * range  # You were caught, as scanner is at the top of travel.

print("SEVERITY:", severity)