class Airplane:
    def __init__(self, airplane_type, passenger_capacity):
        self.airplane_type = airplane_type 
        self.passenger_capacity = passenger_capacity  
        self.current_passengers = 0  

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return NotImplemented

    def __add__(self, number):
        if isinstance(number, int):
            self.current_passengers += number
            if self.current_passengers > self.passenger_capacity:
                self.current_passengers = self.passenger_capacity
            return self.current_passengers
        return NotImplemented

    def __sub__(self, number):
        if isinstance(number, int):
            self.current_passengers -= number
            if self.current_passengers < 0:
                self.current_passengers = 0
            return self.current_passengers
        return NotImplemented

    def __iadd__(self, number):
        return self.__add__(number)

    def __isub__(self, number):
        return self.__sub__(number)

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity > other.passenger_capacity
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity < other.passenger_capacity
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity <= other.passenger_capacity
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passenger_capacity >= other.passenger_capacity
        return NotImplemented

    def __str__(self):
        return f"{self.airplane_type} (Capacity: {self.passenger_capacity}, Current: {self.current_passengers})"


if __name__ == "__main__":
    plane1 = Airplane("Boeing 737", 200)
    plane2 = Airplane("Airbus A320", 180)

    print(plane1)
    print(plane2)

    plane1 += 50
    print("After adding 50 passengers:", plane1)

    plane1 -= 10
    print("After removing 10 passengers:", plane1)

    print(plane1 == plane2)  # False
    print(plane1 > plane2)  # True