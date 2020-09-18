from ua.univer.base.day2.lesson02.hw02 import functions


def main():

    km = int(input("Input kilometres: "))
    result = functions.convert_km_to_miles(km)
    print("Returned value in miles: ", result)


if __name__ == "__main__":
    main()