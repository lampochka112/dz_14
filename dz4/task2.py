class Ship:
    def __init__(self, name, country, tonnage, max_speed):
        """Инициализация корабля"""
        self.name = name  # название корабля
        self.country = country  # страна происхождения
        self.tonnage = tonnage  # водоизмещение (в тоннах)
        self.max_speed = max_speed  # максимальная скорость (в узлах)
        self.is_sailing = False  # состояние корабля (находится в море или нет)

    def sail(self):
        """Запуск корабля в плавание"""
        if not self.is_sailing:
            self.is_sailing = True
            print(f"{self.name} отправился в плавание.")
        else:
            print(f"{self.name} уже в плавании.")

    def dock(self):
        """Прибытие корабля в порт"""
        if self.is_sailing:
            self.is_sailing = False
            print(f"{self.name} пришвартован в порт.")
        else:
            print(f"{self.name} уже в порту.")

    def get_info(self):
        """Информация о корабле"""
        return f"Название: {self.name}, Страна: {self.country}, Водоизмещение: {self.tonnage} т, " \
               f"Макс. скорость: {self.max_speed} узлов"

class Frigate(Ship):
    def __init__(self, name, country, tonnage, max_speed, weapon_system):
        """Инициализация фрегата"""
        super().__init__(name, country, tonnage, max_speed)
        self.weapon_system = weapon_system  # тип оружейной системы (например, ракеты, пушки)

    def engage_enemy(self):
        """Функция для атаки на врага"""
        if self.is_sailing:
            print(f"{self.name} атакует врага с использованием {self.weapon_system}.")
        else:
            print(f"{self.name} не может атаковать, так как находится в порту.")

    def get_info(self):
        """Информация о фрегате (расширенная)"""
        return f"{super().get_info()}, Оружейная система: {self.weapon_system}"

class Destroyer(Ship):
    def __init__(self, name, country, tonnage, max_speed, anti_aircraft_system):
        """Инициализация эсминца"""
        super().__init__(name, country, tonnage, max_speed)
        self.anti_aircraft_system = anti_aircraft_system  # система ПВО

    def launch_countermeasures(self):
        """Запуск контрмер"""
        if self.is_sailing:
            print(f"{self.name} запускает контрмеры для защиты от воздушных угроз.")
        else:
            print(f"{self.name} не может запустить контрмеры, так как находится в порту.")

    def get_info(self):
        """Информация об эсминце (расширенная)"""
        return f"{super().get_info()}, Система ПВО: {self.anti_aircraft_system}"

class Cruiser(Ship):
    def __init__(self, name, country, tonnage, max_speed, cruise_missiles):
        """Инициализация крейсера"""
        super().__init__(name, country, tonnage, max_speed)
        self.cruise_missiles = cruise_missiles  # количество крылатых ракет

    def launch_missile(self):
        """Запуск крылатой ракеты"""
        if self.is_sailing and self.cruise_missiles > 0:
            self.cruise_missiles -= 1
            print(f"{self.name} запускает крылатую ракету. Осталось {self.cruise_missiles} ракет.")
        else:
            print(f"{self.name} не может запустить ракету.")

    def get_info(self):
        """Информация о крейсере (расширенная)"""
        return f"{super().get_info()}, Количество крылатых ракет: {self.cruise_missiles}"

# Пример использования:

# Создание объектов кораблей
frigate = Frigate(name="F-3000", country="USA", tonnage=6000, max_speed=30, weapon_system="RIM-66 Standard")
destroyer = Destroyer(name="D-2000", country="Russia", tonnage=8000, max_speed=32, anti_aircraft_system="S-300")
cruiser = Cruiser(name="C-4000", country="China", tonnage=10000, max_speed=35, cruise_missiles=50)

# Информация о кораблях
print(f"Информация о фрегате: {frigate.get_info()}")
frigate.sail()
frigate.engage_enemy()
frigate.dock()

print(f"\nИнформация об эсминце: {destroyer.get_info()}")
destroyer.sail()
destroyer.launch_countermeasures()
destroyer.dock()

print(f"\nИнформация о крейсере: {cruiser.get_info()}")
cruiser.sail()
cruiser.launch_missile()
cruiser.dock()