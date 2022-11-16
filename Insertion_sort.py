def insertion_sort(matrix):
    count = 0
    for i in range(len(matrix)):
        j = i
        while j > 0 and matrix[j - 1] > matrix[j]:
            count += 1

            temp = matrix[j - 1]
            matrix[j - 1] = matrix[j]
            matrix[j] = temp

            j -= 1
        if j > 0:
            count += 1
    return matrix, count
