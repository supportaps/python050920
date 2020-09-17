from ua.univer.base.day2.lesson02.tasks.task_lib import print_odd_by_range, task02_print_N_K, \
    task03_print_from_a_to_b_with_count, task04_print_10_number_from, task05_factorial, task06_pow, task08_draw_shape

while True:
    answer = int(input("choice number: "))
    if answer == 1 :
        print_odd_by_range(1, 100)
    elif answer == 2 :
        task02_print_N_K(10, 7)
    elif answer == 3 :
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        task03_print_from_a_to_b_with_count(a, b)
    elif answer == 4:
        task04_print_10_number_from()
    elif answer == 5:
        result = task05_factorial(int(input("Enter n: ")))
        print(result)
    elif answer == 6:
        exp_result = 2 ** 10
        act_result = task06_pow(2, 10)
        print("expected = ", exp_result, "actual", act_result)
    elif answer == 8:
        task08_draw_shape()
    elif answer == 0 :
        break