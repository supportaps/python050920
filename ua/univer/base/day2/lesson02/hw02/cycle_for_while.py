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

def traversed_path():

    speed = int(input("Input speed of the train (km / hour) : "))
    hours_to_move = int(input("How many hours it was moving : "))
    step = 1


    for i in range(1,hours_to_move + step, step):
        if i == 1:
            print("hour            path")
            print("--------------------")
        print(i, "             ", speed * i)

def average_thickness_rain():

    months = 12
    step = 1
    years = int(input("Input how many years : "))
    rain = 0

    for year in range(1, years + step, step):
        for month in range(1, months + 1, step):
            rain = int(input("Input raindrops in ml for year: " + str(year) + " and month: "+ str(month) + ": ")) + rain

    print("Months: ", months * years)
    print("Total raindrops in ml: ", rain)
    print("Average raindrops in ml: ", rain / (months * years))

if __name__== '__main__':
    average_thickness_rain()

