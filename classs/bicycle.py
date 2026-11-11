from transport import Transport


class Bicycle(Transport):
    def __init__(self, name, speed, gears):
        super().__init__(name, speed)
        self.gears = gears

    def move(self):
        return f"Велосипед {self.name} едет со скоростью {self.speed} км/ч"

    def get_info(self):
        return f"Велосипед: {self.name}, передачи: {self.gears}"
