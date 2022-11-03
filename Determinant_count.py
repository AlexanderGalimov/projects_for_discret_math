import math


def cut_matrix(matrix, index):
    result = [[0] * (len(matrix) - 1) for _ in range((len(matrix[0]) - 1))]
    a = 0
    for i in range(len(matrix)):
        if a == len(matrix) - 1:
            break
        for j in range(len(matrix[0])):
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
            result_sum = result_sum + matrix[i][0] * int(math.pow(-1, i + 2)) * determinant_count(cut_matrix(matrix, i))
        else:
            result_sum = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    return result_sum
