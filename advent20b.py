# Advent of Code 2017
# Day 20 - Part II
# mushmine - Python


'''
The next part involves tracking collisions, or when two particles occupy the same position per clock tick. My approach is to track all the positions of all the particles per tick, and then remove these from the list of particles. However, instead of manipulating the original list (which is tricky since the loop depends on the size of the list), I create a separate list of non-colliding particles and use that going forward per tick.

We have to use a separate list for all the particle positions, all the collision positions, and all the particles to remove because of the reciprocal and temporal nature of the removal. In other words, once we've determined that a value Y collides with a previous particle X, we have to know to remove both X and Y from the list of particles. However, we can't remove them immediately because we don't know if there will be a Z that also comes into the same position as X and Y, later in the list of particles.
'''

with open("advent20.in", "r") as f: all_file_list = f.readlines()

def parse(this_line):
    return [list(map(int, this_particle[3:-1].split(","))) for this_particle in this_line.strip().split(", ")]

all_particles = [parse(this_line) for this_line in all_file_list]

num = 1
while True:
    all_positions = []  # NEW: Track all positions of particles.
    collisions = []  # NEW: Track which positions have collisions.
    remove_these = []  # NEW: Any particles in these collision positions that need to be removed.

    positions = {}
    delete = []
    for i, this_particle in enumerate(all_particles):
        this_particle[1][0] += this_particle[2][0]
        this_particle[1][1] += this_particle[2][1]
        this_particle[1][2] += this_particle[2][2]
        this_particle[0][0] += this_particle[1][0]
        this_particle[0][1] += this_particle[1][1]
        this_particle[0][2] += this_particle[1][2]

        # NEW: Everything after this point is new code to track collisions.
        this_position = ",".join(map(str, this_particle[0]))  # Position of current particle.
        # print("POS:", this_position)
        if this_position in all_positions: collisions.append(this_position)  # This position has collision(s).
        all_positions.append(this_position)  # Add to list of all positions regardless, to get ID, later.

    # Since we need to get the ID (line number) of each particle, we have to check every line, again.
    for i, this_position in enumerate(all_positions):
        if this_position in collisions: remove_these.append(i)  # Now we have a list if ID's to remove.

    # Instead of actually removing from all_particles (while we loop through it), we just create a new one.
    all_particles = [this_particle for i, this_particle in enumerate(all_particles) if i not in remove_these]

    print("SO FAR [", num, "]:", len(all_particles))
    num += 1
