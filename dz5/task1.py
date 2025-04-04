import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_length(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.get_length() < other.get_length()
        return False

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.get_length() <= other.get_length()
        return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.get_length() > other.get_length()
        return False

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.get_length() >= other.get_length()
        return False

    def __add__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
        return self

    def __sub__(self, other):
        if isinstance(other, Circle):
            self.radius -= other.radius
        return self

    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
        return self

    def __isub__(self, other):
        if isinstance(other, Circle):
            self.radius -= other.radius
        return self

    def __str__(self):
        return f"Окружность с радиусом {self.radius:.2f}, длина: {self.get_length():.2f}"


circle1 = Circle(5)  # Окружность с радиусом 5
circle2 = Circle(7)  # Окружность с радиусом 7

print(circle1)  # Окружность с радиусом 5, длина: 31.42
print(circle2)  # Окружность с радиусом 7, длина: 43.98

# Сравнение радиусов
print(circle1 == circle2)  # False, так как радиусы не равны

# Сравнение длин окружностей
print(circle1 > circle2)  # False, так как длина окружности 1 меньше длины окружности 2
print(circle1 <= circle2)  # True, так как длина окружности 1 меньше или равна длине окружности 2

circle1 += circle2
print(circle1)  # Окружность с радиусом 12, длина: 75.40

circle1 -= circle2
print(circle1)  # Окружность с радиусом 5, длина: 31.42