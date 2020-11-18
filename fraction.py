

class frac:

    @staticmethod
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def __init__(self, num, den=1):
        assert den != 0, "denominator is zero"
        self.num = abs(num)
        self.den = abs(den)
        d = frac.gcd(self.num, self.den)
        self.num //= d
        self.den //= d
        if num * den < 0:
            self.num *= -1

    def __add__(self, other):
        if type(other) == int: other = frac(other)
        return frac(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        if type(other) == int: other = frac(other)
        return frac(self.num * other.den - self.den * other.num, self.den * other.den)

    def __mul__(self, other):
        if type(other) == int: other = frac(other)
        return frac(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if type(other) == int: other = frac(other)
        return frac(self.num * other.den, self.den * other.num)

    def __lt__(self, other):
        if type(other) == int: other = frac(other)
        return self.num * other.den - self.den * other.num < 0
    def __le__(self, other):
        if type(other) == int: other = frac(other)
        return self.num * other.den - self.den * other.num <= 0
    
    def __gt__(self, other):
        if type(other) == int: other = frac(other)
        return self.num * other.den - self.den * other.num > 0
    def __ge__(self, other):
        if type(other) == int: other = frac(other)
        return self.num * other.den - self.den * other.num >= 0

    def __neg__(self):
        return frac(-self.num, self.den)
    
    def __eq__(self, other):
        if type(other) == int: other = frac(other)
        return self.num == other.num and self.den == other.den

    def signstr(self):
        if self.num >= 0:
            return " + "
        return " - "
    def absstr(self):
        return f'{abs(self.num) / self.den:.2f}'
    def valstr(self):
        return self.signstr() + self.absstr()
    def unsignstr(self):
        return f'{self.num / self.den:.2f}'

    def __hash__(self):
        return hash(self.num / self.den)

    def __repr__(self):
        #return f'{self.num / self.den:.2f}'
        if self.num == 0:
            return "0"
        return f'{self.num}/{self.den}'

a = frac(2, 3)
b = frac(1, 2)
c = frac(1081398450, 25248700)