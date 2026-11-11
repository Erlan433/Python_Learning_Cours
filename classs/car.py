from transport import Transport


class Car(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel

    def refuel(self):
        return f"{self.name} заправлен: {self.fuel} л"
