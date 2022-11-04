import Determinant_count
import Insertion_sort
import File_permutations
import Shaker_sort

test_matrix_1 = [[1, 2, 3],
                 [3, 4, 5],
                 [7, 8, 9]]
print(Determinant_count.determinant_count(test_matrix_1))

test = [-3, 2, -1, 3, 9, 6, 8, 7, -10]
print(Insertion_sort.insertion_sort(test))
print(Shaker_sort.shaker_sort(test))

print(Determinant_count.determinant_count(File_permutations.read_two_dimensional_list("src.txt")))
print(Insertion_sort.insertion_sort(File_permutations.read_one_dimensional_list("src.txt")))

File_permutations.write_one_dimensional_matrix_to_file(File_permutations.read_one_dimensional_list("src.txt"), "out.txt")
File_permutations.write_two_dimensional_matrix_to_file(test_matrix_1, "out.txt")

