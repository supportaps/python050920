#В заданиях на формирование матрицы предполагается, что размер резуль-
#тирующей матрицы не превосходит 10 x 10.
#Matrix1. Даны целые положительные числа M и N. Сформировать целочислен-
#ную матрицу размера M x N, у которой все элементы I-й строки имеют зна-
#чение 10·I (I = 1, …, M).

def matrix1(m = 10, n = 10):
    matrix = []
    for i in range(m):
        matrix.append(list()) # instead of list the [] can be used
        for j in range(n):
            matrix[i].append(10 * i)
           # value = int(input("input value: "))
           # matrix[i].append(value)
    print(matrix)

#Matrix2. Даны целые положительные числа M и N. Сформировать целочислен-
#ную матрицу размера M x N, у которой все элементы J-го столбца имеют
#значение 5·J (J = 1, …, N).

def matrix2(m = 4, n = 4):
    matrix = []
    for i in range(m):
        matrix.append(list())
        for j in range(n):
            matrix[i].append(5 * j)
    print(matrix)
    for row in matrix:
        print(row)

#Matrix3. Даны целые положительные числа M, N и набор из M чисел. Сформи-
#ровать матрицу размера M x N, у которой в каждом столбце содержатся все
##числа из исходного набора (в том же порядке).

def matrix3(m = 5, n = 5, arr = [1, 2, 3, 4, 5]):
    matrix = []
    for i in range(m):
        matrix.append(list())
        for j in range(n):
           matrix[i].append(arr[i])
    for row in matrix:
        print(row)


#Matrix4. Даны целые положительные числа M, N и набор из N чисел. Сформи-
#ровать матрицу размера M x N, у которой в каждой строке содержатся все
#числа из исходного набора (в том же порядке).

def matrix4(m = 5, n = 5, arr = [1, 2, 3, 4, 5]):
    matrix = []
    for i in range(m):
        matrix.append(list())
        for j in range(n):
           matrix[i].append(arr[j])
    for row in matrix:
        print(row)
#Matrix5. Даны целые положительные числа M, N, число D и набор из M чисел.
#Сформировать матрицу размера M x N, у которой первый столбец совпада-
#ет  с  исходным  набором  чисел,  а  элементы  каждого  следующего  столбца
#равны сумме соответствующего элемента предыдущего столбца и числа D
#(в результате каждая строка матрицы будет содержать элементы арифме-
#тической прогрессии).

def matrix5(m = 5, n = 5, arr = [1, 2, 3, 4, 5], d = 2):
    matrix = []
    for i in range(m):
        matrix.append(list())
        for j in range(n):
            if j == 0:
                matrix[i].append(arr[i])
            elif j > 0:
                matrix[i].append(matrix[i][j - 1] + d)
    for row in matrix:
        print(row)




#Matrix16*. Дана квадратная матрица A порядка M (M — нечетное число). Начи-
#ная с элемента A1,1 и перемещаясь против часовой стрелки, вывести все ее
#элементы по спирали: первый столбец, последняя строка, последний стол-
#бец  в  обратном  порядке,  первая  строка  в  обратном  порядке,  оставшиеся
#элементы второго столбца и т. д.; последним выводится центральный эле-
#мент матрицы.

if __name__ == '__main__':
    matrix5()