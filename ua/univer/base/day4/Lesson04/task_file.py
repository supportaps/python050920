def read_write_file_example_v1():
    myfile = open("text.txt", "w")
    myfile.write("1,2,3,4,5,6,7,8")
    myfile.close()

    myfile = open("text.txt", "r")
    row = myfile.readline()
    print(row)
    myfile.close()


def read_write_file_example_v2():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    with open("data.txt", "w") as afile:
        for i in range(len(arr)):
            afile.write(str(arr[i]) + ",")

    with open("data.txt", "r") as rfile:
        for row in rfile:
            print(row, end="")


def read_write_file_example_v3():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    with open("data.txt", "w") as afile:
        for i in range(len(arr)):
            afile.write(str(arr[i]) + ",")

    with open("data.txt", "r") as rfile:
        row = rfile.readline()
        mas_row = row.split(',')
        mas_int = []
        for s in mas_row:
            if s != "":
                mas_int.append(int(s))
        print(mas_int)

def matrix_with_file():
    matrix = [[4, 2, 3], [4, 3, 6], [7, 1, 9]]
    with open("matrix.txt", "w") as afile:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cell = str(matrix[i][j])
                afile.write(cell + ",")
            afile.write('/n')

    with open("matrix.txt", "r") as rfile:
        matrix = []
        count_row = 0
        for r in rfile:
            mas_row = r.split(',')
            matrix.append([])
            for s in mas_row:
                if s != "" and s != "\n":
                    matrix[count_row].append(int(s))
            count_row += 1
        print(matrix)




if __name__ == '__main__':
    matrix_with_file()
