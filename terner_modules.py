import string
import itertools


class Experimental:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def product_of_x(self):
        dbd = itertools.product(string.ascii_letters, repeat=self.x)
        return dbd
