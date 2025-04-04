class Money:
    def __init__(self, whole_part=0, fractional_part=0, currency="USD"):
        self.whole_part = whole_part
        self.fractional_part = fractional_part
        self.currency = currency
        self.normalize()  # Нормализуем деньги, если копейки/центы больше 100.

    def normalize(self):
        """Нормализация суммы (если копейки/центы больше 100, то добавляем к целой части)."""
        if self.fractional_part >= 100:
            self.whole_part += self.fractional_part // 100
            self.fractional_part = self.fractional_part % 100

    def set_value(self, whole_part, fractional_part):
        """Устанавливаем значение для целой и дробной части."""
        self.whole_part = whole_part
        self.fractional_part = fractional_part
        self.normalize()

    def get_value(self):
        """Возвращает сумму в виде строки."""
        return f"{self.whole_part} {self.currency} {self.fractional_part:02d}"

    def add(self, other):
        """Добавление суммы денег из другого объекта Money."""
        if self.currency != other.currency:
            raise ValueError("Валюты не совпадают.")
        
        total_whole = self.whole_part + other.whole_part
        total_fractional = self.fractional_part + other.fractional_part
        
        result = Money(total_whole, total_fractional, self.currency)
        return result

    def subtract(self, other):
        """Вычитание суммы денег из другого объекта Money."""
        if self.currency != other.currency:
            raise ValueError("Валюты не совпадают.")
        
        total_whole = self.whole_part - other.whole_part
        total_fractional = self.fractional_part - other.fractional_part
        
        if total_fractional < 0:
            total_whole -= 1
            total_fractional += 100
        
        result = Money(total_whole, total_fractional, self.currency)
        return result

    def multiply(self, factor):
        """Умножение суммы денег на число."""
        total_cents = (self.whole_part * 100 + self.fractional_part) * factor
        result = Money(total_cents // 100, total_cents % 100, self.currency)
        return result

    def divide(self, factor):
        """Деление суммы денег на число."""
        total_cents = (self.whole_part * 100 + self.fractional_part) // factor
        result = Money(total_cents // 100, total_cents % 100, self.currency)
        return result

    def __str__(self):
        """Возвращает строковое представление суммы денег."""
        return self.get_value()


money1 = Money(10, 50, "USD")  # 10 долларов 50 центов
money2 = Money(5, 75, "USD")   # 5 долларов 75 центов

print("Сумма money1:", money1)  # Выводит: 10 USD 50
print("Сумма money2:", money2)  # Выводит: 5 USD 75

# Сложение
money3 = money1.add(money2)
print("Сумма money1 + money2:", money3)  # Выводит: 16 USD 25

# Вычитание
money4 = money1.subtract(money2)
print("Сумма money1 - money2:", money4)  # Выводит: 4 USD 75

# Умножение
money5 = money1.multiply(2)
print("Сумма money1 * 2:", money5)  # Выводит: 21 USD 00

# Деление
money6 = money1.divide(3)
print("Сумма money1 / 3:", money6)  # Выводит: 3 USD 50