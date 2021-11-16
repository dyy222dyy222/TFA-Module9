
class Portfolio:
    def __int__(self):
        self._stock = []

    def buy(self, name, shares, price):
        self._stock.append((name,shares, price))

    def cost(self):
        return sum(
            shares * price for _, shares, price in self._stocks)
        ) 