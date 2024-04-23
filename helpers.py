from person import Person


def get_people(num):
    list_people = []
    for i in range(num):
        person_name = input("Name of person {} ".format(str(i + 1)))
        new_person = Person(name=person_name)
        list_people.append(new_person)
    return list_people


def get_prices(people):
    combined_subtotal = 0
    shared_price = get_shared_prices(len(people))
    for p in people:
        string_prices = input("Enter items purchased by {}: ".format(p.name))
        list_prices = string_prices.split()
        float_prices = [float(i) for i in list_prices]
        p.item_prices = float_prices
        p.subtotal = sum(p.item_prices) + shared_price
        combined_subtotal += p.subtotal
    return combined_subtotal


def get_shared_prices(num_people):
    shared_items = input("Enter shared items: ")
    float_shared_items = [float(i) for i in shared_items.split()]
    shared_price = sum(float_shared_items) / num_people
    return shared_price
    