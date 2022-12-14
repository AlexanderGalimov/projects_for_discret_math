from itertools import *


def quickSort(numbers, left, right):
    counter = 0
    l_border = left
    r_border = right
    pivot = numbers[left]
    while left < right:
        counter = counter + 1
        while (numbers[right] >= pivot) and (left < right):
            counter = counter + 1
            right = right - 1
        if left != right:
            counter = counter + 1
            numbers[left] = numbers[right]
            left = left + 1

        while (numbers[left] <= pivot) and (left < right):
            counter = counter + 1
            left = left + 1
        if left != right:
            counter = counter + 1
            numbers[right] = numbers[left]
            right = right - 1
    numbers[left] = pivot
    pivot = left
    left = l_border
    right = r_border
    if left < pivot:
        counter = counter + 1
        counter = counter + quickSort(numbers, left, pivot - 1)
    if right > pivot:
        counter = counter + 1
        counter = counter + quickSort(numbers, pivot + 1, right)
    return counter


def lambda_quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = list(filter(lambda num: num < pivot, data))
    same = [num for num in data if num == pivot]
    right = list(filter(lambda num: num > pivot, data))

    return lambda_quick_sort(left) + same + lambda_quick_sort(right)


def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + perm[i:]
