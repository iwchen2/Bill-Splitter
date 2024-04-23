class Person:

    def __init__(self, name) -> None:
        self.name = name
        self.item_prices = []
        self.subtotal = 0.0
        self.final_total = 0.0

    
    def get_final_total(self, tax_amount: float, tip_amount: float):
        self.final_total = self.subtotal + tax_amount + tip_amount
        return self.final_total
