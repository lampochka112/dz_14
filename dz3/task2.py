class Fraction:
    _count = 0  

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction._count += 1

    @staticmethod
    def get_count():
        return Fraction._count 

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"



frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
print(Fraction.get_count())  
