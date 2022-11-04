def read_two_dimensional_list(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append([int(x) for x in line.split()])

    return data


def read_one_dimensional_list(file):
    data = []
    with open(file) as f:
        line = f.readline()
        data.extend([int(x) for x in line.split()])

    return data


def write_one_dimensional_matrix_to_file(data, file):
    f = open(file, 'w')
    for i in range(len(data)):
        f.write(str(data[i]) + " ")


def write_two_dimensional_matrix_to_file(data, file):
    f = open(file, 'w')
    for i in range(len(data)):
        for j in range(len(data[0])):
            f.write(str(data[i][j]) + " ")
        f.write("\n")
