class Term:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent

    def evaluate(self, x):
        return self.coefficient * (x ** self.exponent)

class Polynomial:
    def __init__(self):
        self.terms = []

    def add_term(self, coefficient, exponent):
        self.terms.append(Term(coefficient, exponent))

    def evaluate(self, x):
        return sum(term.evaluate(x) for term in self.terms)

# 建立多項式
poly = Polynomial()
poly.add_term(6, 2)
poly.add_term(4, 1)
poly.add_term(2, 0)

# 計算結果
x = 91
result = poly.evaluate(x)
print(f"f({x}) = {result}")
