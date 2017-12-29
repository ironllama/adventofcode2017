with open("advent20a.txt", "r") as f: all_file_list = f.readlines()

def parse(this_line):
    return [list(map(int, this_particle[3:-1].split(","))) for this_particle in this_line.strip().split(", ")]

all_particles = [parse(this_line) for this_line in all_file_list]
# print(all_particles[0])

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

num = 1
while True:
    for this_particle in all_particles:
        this_particle[1][0] += this_particle[2][0]
        this_particle[1][1] += this_particle[2][1]
        this_particle[1][2] += this_particle[2][2]
        this_particle[0][0] += this_particle[1][0]
        this_particle[0][1] += this_particle[1][1]
        this_particle[0][2] += this_particle[1][2]

    min_dis = abs(all_particles[0][0][0]) + abs(all_particles[0][0][1]) + abs(all_particles[0][0][2])
    min_id = 0
    for i, this_particle in enumerate(all_particles):
        this_dis = abs(this_particle[0][0]) + abs(this_particle[0][1]) + abs(this_particle[0][2])
        if this_dis < min_dis:
            min_dis = this_dis
            min_id = i
    print("MIN SO FAR:[", num, "]:", min_id)
    num += 1
