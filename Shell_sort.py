import math


def shell_sort_first(array):
    counter = 0
    step = 2 ** math.floor(math.log2(len(array))) - 1
    while step > 0:
        for i in range(step, len(array)):
            j = i
            curr_elem = array[i]
            while j >= step:
                counter += 1
                if curr_elem < array[j - step]:
                    array[j] = array[j - step]
                    j -= step
                else:
                    break
            array[j] = curr_elem
        step //= 2
    return counter


def shell_sort_second(array):
    counter = 0
    n = math.floor(math.log10(len(array)) / math.log10(3)) + 1
    step = (3 ** n - 1) // 2
    while step > 0:
        for i in range(step, len(array)):
            j = i
            curr_elem = array[i]
            while j >= step:
                counter += 1
                if curr_elem < array[j - step]:
                    array[j] = array[j - step]
                    j -= step
                else:
                    break
            array[j] = curr_elem
        step //= 3
    return counter
