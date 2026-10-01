class Car:
    def __init__(self, model, engine, power, torque, speed, price, year):
        self.model = model
        self.engine = engine
        self.power = power
        self.torque = torque
        self.speed = speed
        self.price = price
        self.year = year

class BMW(Car):
    pass

BMW_car = BMW("BMW M4 Competition", "3.0L 6-cylinder", "510hp", "650Nm", "250km/h", "$74,700", 2021)
print("Car Model: ", BMW_car.model, "Engine: ", BMW_car.engine, "Power: ", BMW_car.power, "Torque: ", BMW_car.torque, "Speed: ", BMW_car.speed, "Price: ", BMW_car.price, "Year: ", BMW_car.year)

class Ferrari(Car):
    pass

Ferrari_car = Ferrari("Ferrari SF90 Stradale", "4.0L twin-turbo V8 + 3 electric motors", "986hp", "800Nm", "340km/h", "$625,000", 2019)
print("Car Model: ", Ferrari_car.model, "Engine: ", Ferrari_car.engine, "Power: ", Ferrari_car.power, "Torque: ", Ferrari_car.torque, "Speed: ", Ferrari_car.speed, "Price: ", Ferrari_car.price, "Year: ", Ferrari_car.year)
