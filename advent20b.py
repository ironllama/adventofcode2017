with open("advent20a.txt", "r") as f: all_file_list = f.readlines()

def parse(this_line):
    return [list(map(int, this_particle[3:-1].split(","))) for this_particle in this_line.strip().split(", ")]

all_particles = [parse(this_line) for this_line in all_file_list]

num = 1
while True:
    all_positions = []
    collisions = []
    remove_these = []

    positions = {}
    delete = []
    for i, this_particle in enumerate(all_particles):
        this_particle[1][0] += this_particle[2][0]
        this_particle[1][1] += this_particle[2][1]
        this_particle[1][2] += this_particle[2][2]
        this_particle[0][0] += this_particle[1][0]
        this_particle[0][1] += this_particle[1][1]
        this_particle[0][2] += this_particle[1][2]

        this_position = ",".join(map(str, this_particle[0]))
        # print("POS:", this_position)
        if this_position in all_positions: collisions.append(this_position)
        all_positions.append(this_position)

    for i, this_position in enumerate(all_positions):
        if this_position in collisions:
            remove_these.append(i)

    all_particles = [this_particle for i, this_particle in enumerate(all_particles) if i not in remove_these]

    print("SO FAR [", num, "]:", len(all_particles))
    num += 1
