def insertion_sort(matrix):
    for i in range(len(matrix)):
        j = i
        while j > 0:
            if matrix[j - 1] > matrix[j]:
                temp = matrix[j - 1]
                matrix[j - 1] = matrix[j]
                matrix[j] = temp
            j -= 1
    return matrix
