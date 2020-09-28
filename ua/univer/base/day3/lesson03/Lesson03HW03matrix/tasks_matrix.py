

matrix_two_dim = [
        [1,2,3,4,5,0,7,8,9,1],
        [-3,4,5,23,0,-6,0,-8,33,2],
        [5,5,5,5,5,5,5,5,5,5],
        [5,5,0,0,0,5,5,5,5,5]
                        ]
def general_cycle_matrix():

    for row in matrix_two_dim:
        for cell in row:
            print(cell)

    for i in range(len(matrix_two_dim)):
    #обработка строки

    #--------------------------
        for j in range(len(matrix_two_dim[i])):
        # обработка ячейки

        # --------------------------
            print(matrix_two_dim[i][j],end="\t")
        # после обработки ячейки

        # --------------------------
        print()
        # --------------------------

#1. Вывести все положительные елементы;

def positive_elements_output_v1(matrix):

    for row in matrix:
        for cell in row:
            if cell > 0:
                print(cell)

def positive_elements_output_v2(matrix):

    for i in range(len(matrix_two_dim)):

        for j in range(len(matrix_two_dim[i])):

            if matrix_two_dim[i][j] > 0:
                print(matrix_two_dim[i][j], end="\t")
            else:
                print("", end="\t")

        print()
    print("END")

#2. Вывести количество строк, не содержащих ни одного нулевого элемента;

def string_without_null_element(matrix):
    string = []
    count_strings = 0
    count_strings_with_null = 0
    check_row = 0
    length = 0

    for row in matrix:
        check_row = row
        for cell in row:
            if cell == 0 and check_row == row:
                string.append(row)

        count_strings += 1

    length = len(string)

    for i in range(len(string) - 1):
        if string[i] != string[i+1] and i <= length - 1:
            count_strings_with_null +=1

    print("Number of strings without zero is: ", count_strings - count_strings_with_null + 1)

#7. Характеристикой строки целочисленной матрицы
#назовем сумму ее положительных четных элементов.
#  Переставляя строки заданной матрицы,
#расположить их в соответствии с ростом характеристик.

def order_rows_by_sum_odd_elem(matrix_two_dim):

    list_sum_row = []
    sum_matrix = 0
    for i in range(len(matrix_two_dim)):
    #обработка строки
        sum_row = 0
    #------------------------
        for j in range(len(matrix_two_dim[i])):
        # обработка ячейки
            if matrix_two_dim[i][j] > 0  and matrix_two_dim[i][j] % 2 == 0:
                sum_row += matrix_two_dim[i][j]
        # --------------------------

        # после обработки ячейки
        print("row", i, " = ", sum_row)
        sum_matrix += sum_row
        list_sum_row.append(sum_row)
        # --------------------------
    print("Sum matrix: ", sum_matrix)
    print(list_sum_row)
    for i in range(len(list_sum_row)):
        print(list_sum_row[i])
        for j in range(len(list_sum_row) - 1 - i):

            if (list_sum_row[j] < list_sum_row[j + 1]):
                temp = list_sum_row[j]
                temp_row = matrix_two_dim[j]
                list_sum_row[j] = list_sum_row[j + 1]
                matrix_two_dim[j] = matrix_two_dim[j + 1]
                list_sum_row[j + 1] = temp
                matrix_two_dim[j + 1] = temp_row

    print(list_sum_row)
    for row in matrix_two_dim:
        for cell in row:
            print(cell, end = "\t")
        print()











if __name__ == '__main__':
    order_rows_by_sum_odd_elem(matrix_two_dim)