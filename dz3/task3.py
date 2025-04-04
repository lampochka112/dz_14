class UnitConverter:

    @staticmethod
    def meters_to_feet(meters):
        """Перевод метров в футы"""
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        """Перевод футов в метры"""
        return feet / 3.28084

    @staticmethod
    def meters_to_inches(meters):
        """Перевод метров в дюймы"""
        return meters * 39.3701

    @staticmethod
    def inches_to_meters(inches):
        """Перевод дюймов в метры"""
        return inches / 39.3701

    @staticmethod
    def kilometers_to_miles(kilometers):
        """Перевод километров в мили"""
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        """Перевод миль в километры"""
        return miles / 0.621371

# Пример использования:
meters = 5
feet = UnitConverter.meters_to_feet(meters)
print(f"{meters} метров = {feet} футов")

miles = 10
kilometers = UnitConverter.miles_to_kilometers(miles)
print(f"{miles} миль = {kilometers} километров")