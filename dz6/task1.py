import math

class Figura:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен в производных классах.")

class Pryamougolnik(Figura):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Krug(Figura):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class PryamougolnyTreugolnik(Figura):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Trapeziya(Figura):
    def __init__(self, a, b, height):
        self.a = a  # длина основания 1
        self.b = b  # длина основания 2
        self.height = height

    def area(self):
        return 0.5 * (self.a + self.b) * self.height

if __name__ == "__main__":
    rectangle = Pryamougolnik(5, 10)
    print(f"Площадь прямоугольника: {rectangle.area()}")

    circle = Krug(7)
    print(f"Площадь круга: {circle.area()}")

    right_triangle = PryamougolnyTreugolnik(6, 8)
    print(f"Площадь прямоугольного треугольника: {right_triangle.area()}")

    trapezoid = Trapeziya(5, 7, 4)
    print(f"Площадь трапеции: {trapezoid.area()}")