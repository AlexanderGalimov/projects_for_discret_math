import math


def insertion_sort(arr, left, right):
    for i in range(left, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, left, right):
    pivot = arr[left]
    left_border = left
    right_border = right
    while left_border <= right_border:
        while arr[right_border] >= pivot:
            right_border = right_border - 1
        while arr[left_border] <= pivot:
            left_border = left_border + 1
        arr[left_border], arr[right_border] = arr[right_border], arr[left_border]
    arr[left_border], arr[right_border] = arr[right_border], arr[left_border]
    arr[left], arr[right_border] = arr[right_border], arr[left]
    return right_border


def select_opt(arr, k, left, right):
    w = 5
    while 1:
        d = right - left + 1
        if d <= w:
            insertion_sort(arr, left, right)
            result = left + k - 1
            return result
        dd = math.floor(d / w)
        for i in range(1, dd):
            insertion_sort(arr, left + (i - 1) * w, left + i * w - 1)
            swap(arr, left + i - 1, left + (i - 1) * w + math.ceil(w / 2) - 1)
        v = select_opt(arr, math.ceil(dd / 2), left, left + dd - 1)
        swap(arr, left, v)
        v = partition(arr, left, right)
        temp = v - left + 1
        if k < temp:
            right = v - 1
        elif k > temp:
            k = k - temp
            left = v + 1
        else:
            result = v
            return result
