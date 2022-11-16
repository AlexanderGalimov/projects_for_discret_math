def shaker_sort(matrix):
    count = 0
    left = 0
    right = len(matrix) - 1
    flag = True
    while flag and (left < right):
        flag = False
        for i in range(left, right, +1):
            count += 1
            if matrix[i] > matrix[i + 1]:
                t = matrix[i]
                matrix[i] = matrix[i + 1]
                matrix[i + 1] = t
                flag = True
        right -= 1

        for i in range(right, left, -1):
            count += 1
            if matrix[i - 1] > matrix[i]:
                t = matrix[i - 1]
                matrix[i - 1] = matrix[i]
                matrix[i] = t
                flag = True
        left += 1

    return matrix, count


def shaker_sort2(matrix):
    count = 0
    left = 0
    right = len(matrix) - 1
    left_go_swap = 0
    right_go_swap = len(matrix) - 1
    flag = True
    while flag and (left < right):
        flag = False
        for i in range(left, right, +1):
            count += 1
            if matrix[i] > matrix[i + 1]:
                t = matrix[i]
                matrix[i] = matrix[i + 1]
                matrix[i + 1] = t
                left_go_swap = i
                flag = True

        if left_go_swap < right - 1:
            right = left_go_swap
        else:
            right -= 1

        for i in range(right, left, -1):
            count += 1
            if matrix[i - 1] > matrix[i]:
                t = matrix[i - 1]
                matrix[i - 1] = matrix[i]
                matrix[i] = t
                right_go_swap = i
                flag = True

        if right_go_swap > left + 1:
            left = right_go_swap
        else:
            left += 1

    return matrix, count
