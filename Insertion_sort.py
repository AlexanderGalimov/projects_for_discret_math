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


def insertion_sort_from_to(matrix, start_index, end_index):
    for i in range(start_index, end_index + 1):
        j = i
        while j > start_index and matrix[j - 1] > matrix[j]:

            temp = matrix[j - 1]
            matrix[j - 1] = matrix[j]
            matrix[j] = temp

            j -= 1
    return matrix
