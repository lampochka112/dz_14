class Автомобиль:
    def __init__(self, марка, модель, год, цвет, цена):
        
        self.марка = марка
        self.модель = модель
        self.год = год
        self.цвет = цвет
        self.цена = цена

    def __str__(self):
    
        return f"{self.марка} {self.модель} ({self.год}) - Цвет: {self.цвет}, Цена: {self.цена} руб."

    def __eq__(self, другой_автомобиль):
    
        return (self.марка == другой_автомобиль.марка and
                self.модель == другой_автомобиль.модель and
                self.год == другой_автомобиль.год)

    def __lt__(self, другой_автомобиль):
        
        return self.цена < другой_автомобиль.цена

авто1 = Автомобиль("Toyota", "Camry", 2021, "Черный", 2000000)
авто2 = Автомобиль("Toyota", "Camry", 2021, "Белый", 1800000)
авто3 = Автомобиль("Honda", "Civic", 2022, "Синий", 2100000)

print(авто1)  
print(авто1 == авто2)  
print(авто1 < авто3)   