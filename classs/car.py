from transport import Transport


class Car(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel

    def move(self):
        return f"Автомобиль {self.name} едет со скоростью {self.speed} км/ч"

    def get_info(self):
        return f"Автомобиль: {self.name}, топливо: {self.fuel} л"
