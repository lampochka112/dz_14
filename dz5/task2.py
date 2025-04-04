class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  
        self.imag = imag 

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denom = other.real ** 2 + other.imag ** 2
            real_part = (self.real * other.real + self.imag * other.imag) / denom
            imag_part = (self.imag * other.real - self.real * other.imag) / denom
            return ComplexNumber(real_part, imag_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"

if __name__ == "__main__":
    a = ComplexNumber(1, 2)
    b = ComplexNumber(3, 4)

    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)