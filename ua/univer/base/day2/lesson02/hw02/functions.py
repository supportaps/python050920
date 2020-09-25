def convert_km_to_miles(km):
    print("Miles: ", round(0.6214 * km, 2))
    return round(0.6214 * km, 2)


def tax_from_selling(total_purchase, FEDERAL_TAX, REGIONAL_TAX):
    tax_f = tax_federal(total_purchase, FEDERAL_TAX)
    tax_r = tax_regional(total_purchase, REGIONAL_TAX)
    tax_t = tax_total(tax_f, tax_r)
    sell_t = sell_total(total_purchase, tax_t)

    print(" Sum of the purchase = ", tax_f)
    print(" Federal tax = ", tax_r)
    print(" Total tax = ", tax_t)
    print(" Total = ", sell_t)


def tax_federal(total_purchase, FEDERAL_TAX):
    return total_purchase * FEDERAL_TAX


def tax_regional(total_purchase, REGIONAL_TAX):
    return total_purchase * REGIONAL_TAX


def tax_total(tax_f, tax_r):
    return tax_f + tax_r


def sell_total(total_purchase, tax_t):
    return total_purchase + tax_t
