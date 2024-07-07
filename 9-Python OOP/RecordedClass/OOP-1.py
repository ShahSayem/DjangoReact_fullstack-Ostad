import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        self.numerator = numerator
        self.denominator = denominator

    def add(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        num = ((lcm/self.denominator)*self.numerator) + ((lcm/f.denominator)*f.numerator)
        
        self.numerator = int(num)
        self.denominator = int(lcm)

    def reduceFraction(self):
        g1 = math.gcd(self.numerator, self.denominator)

        self.numerator //= g1
        self.denominator //= g1

    #Define "+" operation (Operator overloading)
    def __add__(self, f): #sub, mul, div are also similar
        lcm = math.lcm(self.denominator, f.denominator)
        num = ((lcm/self.denominator)*self.numerator) + ((lcm/f.denominator)*f.numerator)

        return Fraction(int(num), lcm)
    
    #Define print statement
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    #Define eqality
    def __eq__(self, f):
        return ((self.numerator / self.denominator) == (f.numerator / f.denominator))

    #Define ">"
    def __gt__(self, f):
        return ((self.numerator / self.denominator) > (f.numerator / f.denominator))

    #Define "<"
    def __lt__(self, f):    
        return ((self.numerator / self.denominator) < (f.numerator / f.denominator))
    

f1 = Fraction(10, 2)
print(f1.numerator, f1.denominator)
print(f1)

f2 = Fraction(50, 100)

# f1.add(f2)
# print(f1)

result = f1 + f2
print(result.numerator, result.denominator, result)

print(1+3)

print(f1 != f2)

print(f1 > f2)

print(f1 < f2)

f1.reduceFraction()
f2.reduceFraction()
print(f1, f2)