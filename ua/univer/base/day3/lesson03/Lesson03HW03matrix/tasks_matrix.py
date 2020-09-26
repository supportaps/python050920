
#1. Вывести все положительные елементы;

matrix_two_dim = [
    [1,2,3,4,5,0,7,8,9,1],
    [-3,4,5,23,0,-6,0,-8,33,2],
    [5,5,5,5,5,5,5,5,5,5],
    [5,5,0,0,0,5,5,5,5,5]
]

#1. Вывести все положительные елементы;

def positive_elements_output(matrix):

    for row in matrix:
        for cell in row:
            if cell > 0:
                print(cell)

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









if __name__ == '__main__':
    string_without_null_element(matrix_two_dim)