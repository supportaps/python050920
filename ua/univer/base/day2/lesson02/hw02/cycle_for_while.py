def the_bug_collector_problem():

    days = int(input("How many days? "))
    errors = 0

    for i in range(days):
        errors = int(input("How many errors are today? ")) + errors
    print(" The total number of errors is: ", errors)







if __name__== '__main__':
    the_bug_collector_problem()