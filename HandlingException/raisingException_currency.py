# USD 20
# USD 30
# USD 50


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception("Currency Do Not Match")

        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


value1 = Currency("USD", 20)
value2 = Currency("MXN", 30)
print(value1 + value2)
