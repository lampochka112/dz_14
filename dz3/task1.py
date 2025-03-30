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

if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(5, 6)

    print("Количество созданных дробей:", Fraction.get_count())
