class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power  
        self.is_on = False 

    def turn_on(self):
        """Включение устройства"""
        if not self.is_on:
            self.is_on = True
            print(f"{self.model} включен.")
        else:
            print(f"{self.model} уже включен.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.model} выключен.")
        else:
            print(f"{self.model} уже выключен.")

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Мощность: {self.power} Вт"

class Blender(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity  # емкость в литрах

    def blend(self, ingredients):
      
        if self.is_on:
            print(f"Блендер смешивает {ingredients}...")
        else:
            print("Для смешивания нужно включить блендер.")

    def get_info(self):
        return f"{super().get_info()}, Емкость: {self.capacity} литров"

class MeatGrinder(Device):
    def __init__(self, brand, model, power, grinding_capacity):
        super().__init__(brand, model, power)
        self.grinding_capacity = grinding_capacity  # производительность (кг/мин)

    def grind(self, meat):
        if self.is_on:
            print(f"Мясорубка измельчает {meat}...")
        else:
            print("Для измельчения нужно включить мясорубку.")

    def get_info(self):
        return f"{super().get_info()}, Производительность: {self.grinding_capacity} кг/мин"


blender = Blender(brand="Philips", model="HR2041", power=600, capacity=1.5)
print(blender.get_info())
blender.turn_on()
blender.blend("фрукты и овощи")
blender.turn_off()

meat_grinder = MeatGrinder(brand="Bosch", model="MFW66020", power=1200, grinding_capacity=2.5)
print(meat_grinder.get_info())
meat_grinder.turn_on()
meat_grinder.grind("мясо")
meat_grinder.turn_off()