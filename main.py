import Determinant_count
import Insertion_sort
import File_permutations
import Quick_sort_task
import Search_num

import SelectOpt
import Shaker_sort

# test_matrix_1 = [[1, 2, 8],
#                  [3, 4, 5],
#                  [7, 8, 9]]
# print(Determinant_count.determinant_count(test_matrix_1))
#
# test = [-3, 2, -1, 3, 9, 6, 8, 7, -10]
# print(Insertion_sort.insertion_sort(test))
# print(Shaker_sort.shaker_sort(test))
#
# print(Determinant_count.determinant_count(File_permutations.read_two_dimensional_list("src.txt")))
# print(Insertion_sort.insertion_sort(File_permutations.read_one_dimensional_list("src.txt")))
#
# File_permutations.write_one_dimensional_matrix_to_file(File_permutations.read_one_dimensional_list("src.txt"),
# "out.txt") File_permutations.write_two_dimensional_matrix_to_file(test_matrix_1, "out.txt")
# print(Quick_sort_task.quickSort(data, 0, len(data) - 1))
# data2, count = Insertion_sort.insertion_sort(data)
# print(Search_num.interpolation_search(data2))

# data1, count = Shaker_sort.shaker_sort2(data)
# File_permutations.write_one_dimensional_matrix_to_file(data1, count, "out.txt")

# second
# data = File_permutations.read_one_dimensional_list("src.txt")
# count = 0
# maximum_of_iters = 0
# for i in Quick_sort_task.permutations(data):
#     count = Quick_sort_task.quickSort(i, 0, len(i) - 1)
#     if count > maximum_of_iters:
#         maximum_of_iters = count
#     print(count)
# print("--------")
# print(maximum_of_iters)

#first
# import Shell_sort
#
# data = File_permutations.read_one_dimensional_list("src.txt")
# count_first = Shell_sort.shell_sort_first(data)
# count_second = Shell_sort.shell_sort_second(data)
# File_permutations.write_one_dimensional_matrix_to_file(data, count_first, "out1.txt")
# File_permutations.write_one_dimensional_matrix_to_file(data, count_second, "out2.txt")

data = File_permutations.read_one_dimensional_list("src.txt")
# print(selectOptional.partition(data, 0, len(data) - 1))
# print(Insertion_sort.insertion_sort_from_to(data, 1, 4))
print(data[SelectOpt.select_opt(data,8,0,7)])





