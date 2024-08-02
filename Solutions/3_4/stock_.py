import reader
from tableformat import print_table
from pathlib import Path
 
class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares 
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}, but got {type(value).__name__}')
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}, but got {type(value).__name__}')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == "__main__":
    
    # data_path = Path('Data/portfolio.csv').resolve()
    # portfolio = reader.read_csv_as_instances(data_path, Stock)
    # print_table(portfolio, ['name', 'shares', 'price'])
    s = Stock.from_row(['GOOG', 100, 490.10])
    # s.price = "-100"
    s.case = "study"