def the_bug_collector_problem():

    days = int(input("How many days? "))
    errors = 0

    for i in range(days):
        errors = int(input("How many errors are today? ")) + errors
    print(" The total number of errors is: ", errors)

def the_birned_callories():

    callories_per_min = 4.2
    step = 5
    for i in range(10, 30 + step, step):
        print("Birned callories per", i, "minutes is: ", i * callories_per_min)


def budget_analyze():

    sum_per_month = int(input("Input total sum for one month: "))
    number_of_expenses = int(input("Input number of expences for per one month: "))
    step = 1
    sum_expences = 0
    for i in range(1, number_of_expenses + step, step):
        name_of_the_expance, value_expanse = input("Input name and value: ").split()
        sum_expences = sum_expences + int(value_expanse)
    if sum_expences > sum_per_month:
        print(" The expanse is overspared ", sum_expences  - sum_per_month)
    else:
        print(" The rest you saved: ", sum_per_month - sum_expences)

if __name__== '__main__':
    budget_analyze()