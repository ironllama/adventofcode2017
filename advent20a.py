# Advent of Code 2017
# Day 20 - Part I
# mushmine - Python


'''
At first, I thought I would just try to determine which particle had the smallest acceleration vector. However after submitting a couple wrong answers and considering that it still does not take into account the position of the particle, which is the whole point of the puzzle, it would only work in limited cases, and as it so happened, my puzzle set was one of those cases. I've left in the code, if anyone else wants to play with it.

The second approach was to see how fast the 'closest' particle would change, or if it started to become evident as other particles swung out of the ballpark over time. Fortunately, it became pretty quickly evident that one particular particle held onto the position of being 'closest' and it turns out that it was the answer! Yay for brute-force!
'''

with open("advent20.in", "r") as f: all_file_list = f.readlines()

def parse(this_line):  # Helper function to cut up each line in the file into a multi-dimensional list.
    return [list(map(int, this_particle[3:-1].split(","))) for this_particle in this_line.strip().split(", ")]

all_particles = [parse(this_line) for this_line in all_file_list]  # Process each line, using the helper above.
# print(all_particles[0])

'''
This was the first attempt, trying to just determine which particle had the smallest acceleration vector. Unfortunately, it did not yield the correct answer. :(
'''
# low_acc_list = []
# lowest_acc_v = 0
# for i in range(len(all_file_list)):
#     acc_vector = (abs(all_particles[i][2][0]**2) + abs(all_particles[i][2][1]**2) + abs(all_particles[i][2][2]**2))**0.5
#     if lowest_acc_v == 0 or acc_vector == lowest_acc_v:
#         low_acc_list.append(i)
#         lowest_acc_v = acc_vector
#     elif acc_vector < lowest_acc_v:
#         low_acc_list = [i]
#         lowest_acc_v = acc_vector
# print("LOWEST ACC VEC:", lowest_acc_v, "LIST:", low_acc_list)

'''
This was the second attempt, but just brute-force -- move each particle, then determine position of each particle, and print the closest, and use my own fleshy eyes to see how fast it would change or stay the same.
'''
num = 1  # Used solely for display, to show how many times the loop has run.
while True:
    for this_particle in all_particles:
        # Use the acceleration to change the velocity.
        this_particle[1][0] += this_particle[2][0]
        this_particle[1][1] += this_particle[2][1]
        this_particle[1][2] += this_particle[2][2]

        # Use the velocity to change the position.
        this_particle[0][0] += this_particle[1][0]
        this_particle[0][1] += this_particle[1][1]
        this_particle[0][2] += this_particle[1][2]

    # First, set the min to the first position, as an initial value.
    min_dis = abs(all_particles[0][0][0]) + abs(all_particles[0][0][1]) + abs(all_particles[0][0][2])
    min_id = 0  # To store the ID of the particle we're looking for.
    for i, this_particle in enumerate(all_particles):  # Enumerate to get an index number, with value.
        # Get the distance of this particle.
        this_dis = abs(this_particle[0][0]) + abs(this_particle[0][1]) + abs(this_particle[0][2])

        if this_dis < min_dis:  # We've found something closer to 0 than current min!
            min_dis = this_dis
            min_id = i
    
    print("MIN SO FAR:[", num, "]:", min_id)
    num += 1
