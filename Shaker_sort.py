def shaker_sort(matrix):
    left = 0
    right = len(matrix) - 1
    flag = True
    while flag and (left < right):
        flag = False
        for i in range(left, right, +1):
            if matrix[i] > matrix[i + 1]:
                t = matrix[i]
                matrix[i] = matrix[i + 1]
                matrix[i + 1] = t
                flag = True
        right -= 1

        for i in range(right, left, -1):
            if matrix[i - 1] > matrix[i]:
                t = matrix[i - 1]
                matrix[i - 1] = matrix[i]
                matrix[i] = t
                flag = True
        left += 1

    return matrix
