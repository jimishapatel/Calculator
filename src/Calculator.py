import math


def addition(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    return c





class Calculator:
    result = 0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result