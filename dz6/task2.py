import math

class Figura:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен в производных классах.")

    def __int__(self):
        return int(self.area())

class Pryamougolnik(Figura):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, высота = {self.height}, площадь = {self.area()}"

class Krug(Figura):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Круг: радиус = {self.radius}, площадь = {self.area()}"
    
class PryamougolnyTreugolnik(Figura):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Прямоугольный треугольник: основание = {self.base}, высота = {self.height}, площадь = {self.area()}"


class Trapeziya(Figura):
    def __init__(self, a, b, height):
        self.a = a  # длина основания 1
        self.b = b  # длина основания 2
        self.height = height

    def area(self):
        return 0.5 * (self.a + self.b) * self.height

    def __str__(self):
        return f"Трапеция: основание 1 = {self.a}, основание 2 = {self.b}, высота = {self.height}, площадь = {self.area()}"

if __name__ == "__main__":
    rectangle = Pryamougolnik(5, 10)
    print(rectangle)  
    print(f"Площадь прямоугольника (как int): {int(rectangle)}")  

    circle = Krug(7)
    print(circle)
    print(f"Площадь круга (как int): {int(circle)}")

    right_triangle = PryamougolnyTreugolnik(6, 8)
    print(right_triangle)
    print(f"Площадь прямоугольного треугольника (как int): {int(right_triangle)}")

    trapezoid = Trapeziya(5, 7, 4)
    print(trapezoid)
    print(f"Площадь трапеции (как int): {int(trapezoid)}")