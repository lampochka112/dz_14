class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    # Метод для ввода данных
    def input_data(self):
        self.model = input("Введите модель автомобиля: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя (л): "))
        self.color = input("Введите цвет автомобиля: ")
        self.price = float(input("Введите цену автомобиля: "))

    # Метод для вывода данных
    def output_data(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} руб")

    # Методы доступа к полям
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


# Пример использования
car = Car("Tesla 3", 2022, "Tesla", 2.5, "Белый", 3500000)
car.output_data()

# Изменение данных
car.set_price(3400000)
car.set_color("Черный")
car.output_data()
