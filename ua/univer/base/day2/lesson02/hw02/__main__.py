from ua.univer.base.day2.lesson02.hw02 import functions


def main():

    answer = int(input("Input number: "))

    if answer == 1:
        km = int(input("Input kilometres: "))
        result = functions.convert_km_to_miles(km)
        print("Returned value in miles: ", result)
    elif answer == 2:
        total_purchase = float(input(" Input a purchase: "))
        FEDERAL_TAX = 0.025
        REGIONAL_TAX = 0.05
        functions.tax_from_selling(total_purchase, FEDERAL_TAX, REGIONAL_TAX)

if __name__ == "__main__":
    main()