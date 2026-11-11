from transport import Transport


class Bicycle(Transport):
    def __init__(self, name, speed, gears):
        super().__init__(name, speed)
        self.gears = gears

    def ring_bell(self):
        return f"{self.name}: дзинь-дзинь!"
