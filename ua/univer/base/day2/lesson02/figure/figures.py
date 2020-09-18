def square_1():

    for i in range(10):
        for j in range(10):
            if (j > 0 and j < 9) and (i > 0 and i < 9):
                print("  ",end = "")
            else:
                print("* ",end = "")
        print()

def square_2():

    for i in range(10):
        symbol2 = "*" + "  " + symbol2

    for l in range(len(symbol2) - 4):
        space = str(i).replace(str(i), " ") + space

    for j in range(10):
        if j == 0:
            print(symbol2)
        elif j >= 1 and j <= 8:
            print("*" + space + "*")
        elif j == 9:
            print(symbol2)


def rectangular_triangle_1():

    for i in range(10):
        for j in range(10):
            if i >= j:
                print(" * ", end = "")
        print()


def rectangular_triangle_2():

    symbol2 = ""
    for i in range(10):
        symbol2 = "*" + "  " + symbol2
        print(symbol2)

def equiateral_triangle():

    for i in range(10):
        for j in range(10):
            if j < i:
                print(" * ", end="")
            if i < j:
                print("   ", end="")
            if i > j:
                print("   ", end="")
        print()





if __name__== '__main__':
    equiateral_triangle()