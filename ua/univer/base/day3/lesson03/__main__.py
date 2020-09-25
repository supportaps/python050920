# точка запуска в рамках этого пакета
from ua.univer.base.day3.lesson03.tasks.tasks_list import task2


def list_tasks_00():
    global index
    apples = ["red", "green"]
    apples.append("yellow")
    apples.insert(0, "blue")
    apples.remove("green")
    index = apples.index("red")
    print(apples.index("red"))
    apples[index] = "orange"
    print(apples)
    for x in apples:
        if x != "red":
            print(x)
    objects = [1, 2.6, "Hello", True]
    print(objects)
    for y in objects:
        print(y)
    objects[0] = "Vasya"
    print(objects)
    for i in range(len(apples)):
        print(i)
        print("apples[", i, "]=", apples[i])
    w = 0
    while w < len(objects):
        print(objects[w], 'while')
        w += 1


if __name__ == '__main__':
    task2()