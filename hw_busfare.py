class Vehicle:
    def __init__(self, fare, passengers):
        self.fare = fare
        self.passengers = passengers


class Bus(Vehicle):
    def total_fare(self):
        return self.fare * self.passengers


bus = Bus(20, 5)

print(bus.total_fare())