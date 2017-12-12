import math  # For sqrt() and pow().

input = 347991

nums_per_side = int(math.sqrt(input))
nums_per_side += 1 if nums_per_side % 2 == 0 else 2  # Go up to the next odd number.

last_num = math.pow(nums_per_side, 2)

outer_level = (nums_per_side // 2) + 1

print("INPUT:", input, "NUMS_PER_SIDE:", nums_per_side, "LAST_NUM:", last_num, "OUTER_LEVEL:", outer_level)

# Find the mid or center number at the the axis -- wherever X or Y is 0 in a coordinate system
mid = last_num - (nums_per_side // 2)  # Find bottom center.
shortest_distance = nums_per_side  # The nums_per_side should always be larger than the shortest_distance to an axis.
for i in range(4):  # For each mid or center point counter-clockwise: bottom center, left center, top center, right center.
    if (abs(mid - input) < shortest_distance):
        shortest_distance = abs(mid - input)
    mid = (mid - nums_per_side) + 1  # Next mid or center point.

steps = shortest_distance + outer_level - 1  # Distance to a mid or center axis, and then to the overall center.
print("Number of steps to 1:", steps)
