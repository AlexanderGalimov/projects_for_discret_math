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


def read_one_dimensional_list(file):
    data = []
    with open(file) as f:
        line = f.readline()
        data.extend([int(x) for x in line.split()])

    return data


def write_one_dimensional_matrix_to_file(data, count, file):
    f = open(file, 'w')
    for i in range(len(data)):
        f.write(str(data[i]) + " ")
    f.write("\n" + str(count))
