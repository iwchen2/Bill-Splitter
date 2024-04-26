from person import Person
from helpers import *

'''
    Steps:
    1) Input number of people for bill
    2) Input item/price of each item for each individual(Optional: name each individual)
    3) Input sales tax amount, either as percentage based on location, or just enter raw amount
    4) Input tip
    5) Calculate each individuals total fare 3including tip + tax
'''


def main():
    num_people = int(input("Number of people in party: "))
    list_of_people = get_people(num_people)

    # Retrieve each person's item via prices
    subtotal = get_prices(list_of_people)

    total_tax = float(input("Enter Sales Tax Amount: "))
    total_tip = float(input("Enter Tip Amount: "))
    total_bill = 0.0
    
    # Calculate each person's total w/ tip + tax
    for p in list_of_people:
        percent_of_total = p.subtotal/subtotal
        tip_amount = percent_of_total * total_tip
        tax_amount = percent_of_total * total_tax
        final_total = p.get_final_total(tax_amount, tip_amount)
        total_bill += final_total
        print("{} owes {}".format(p.name, p.final_total))

    print("Total: ${}".format(total_bill))


if __name__ == "__main__":
    main()