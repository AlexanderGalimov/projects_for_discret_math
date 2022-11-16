import math


def cut_matrix(matrix, index):
    result = [[0] * (len(matrix) - 1) for _ in range((len(matrix[0]) - 1))]
    a = 0
    for i in range(len(matrix)):
        if a == len(matrix) - 1:
            break
        for j in range(1, len(matrix[0])):
            if i != index:
                result[a][j - 1] = matrix[i][j]

        if i != index:
            a += 1

    return result


def determinant_count(matrix):
    result_sum = 0
    if len(matrix) == 1:
        return matrix[0][0]

    for i in range(len(matrix)):
        if len(matrix) > 2:
            result_sum = result_sum + matrix[i][0] * int(math.pow(-1, i)) * determinant_count(cut_matrix(matrix, i))
        else:
            result_sum = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    return result_sum


def read_two_dimensional_list(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append([int(x) for x in line.split()])

    return data


def write_two_dimensional_matrix_to_file(data, file):
    f = open(file, 'w')
    for i in range(len(data)):
        for j in range(len(data[0])):
            f.write(str(data[i][j]) + " ")
        f.write("\n")


test_matrix_1 = [[8, 2, 3],
                 [3, 4, 5],
                 [7, 8, 9]]
print(determinant_count(test_matrix_1))
