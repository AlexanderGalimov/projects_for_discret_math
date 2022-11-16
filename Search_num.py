def consistent_search(data):
    result_sum = 0
    for i in range(len(data)):
        result_sum += search_single_num_for_consistent_search(data, data[i])
    average_value = result_sum / len(data)
    return average_value


def search_single_num_for_consistent_search(data, curr_num):
    count_of_iterations = 0
    for i in range(len(data)):
        count_of_iterations += 1
        if curr_num == data[i]:
            return count_of_iterations


def binary_search(sorted_data):
    result_sum = 0
    for i in range(len(sorted_data)):
        result_sum += search_single_num_for_binary_search(sorted_data, sorted_data[i])
    average_sum = result_sum / len(sorted_data)
    return average_sum


def search_single_num_for_binary_search(sorted_data, value):
    result_sum = 0
    flag = False
    left_border = 0
    right_border = len(sorted_data) - 1

    while (left_border <= right_border) and not flag:
        result_sum += 1
        middle = int((left_border + right_border) / 2)
        if sorted_data[middle] == value:
            flag = True
        if sorted_data[middle] > value:
            right_border = middle - 1
        else:
            left_border = middle + 1

    return result_sum


def interpolation_search(sorted_data):
    result_sum = 0
    for i in range(len(sorted_data)):
        result_sum += search_single_num_for_interpolation_search(sorted_data, sorted_data[i])
    average_sum = result_sum / len(sorted_data)
    print(result_sum)
    return average_sum


def search_single_num_for_interpolation_search(sorted_data, value):
    result_sum = 0
    flag = False
    left_border = 0
    right_border = (len(sorted_data) - 1)
    while left_border <= right_border and not flag:
        result_sum += 1
        index = left_border + int(((float(right_border - left_border) / (sorted_data[right_border] - sorted_data[left_border])) * (value - sorted_data[left_border])))
        if sorted_data[index] == value:
            flag = True
        if sorted_data[index] < value:
            left_border = index + 1
        else:
            right_border = index - 1

    return result_sum
