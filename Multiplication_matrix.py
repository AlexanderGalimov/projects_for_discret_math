def multiplication_matrix(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b[0]) and len(matrix_b) != len(matrix_a[0]):
        print("количество столбцов одной матрицы должно соответствовать количеству строк другой")
        return

    height = max(len(matrix_a), len(matrix_b))
    length = max(len(matrix_a[0]), len(matrix_b[0]))
    minimal = min(len(matrix_a), len(matrix_a[0]))

    result = [[0] * height for _ in range(length)]

    for i in range(0, height):
        for j in range(0, length):
            result_sum = 0
            for k in range(0, minimal):
                result_sum = result_sum + matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = result_sum

    print(result)
