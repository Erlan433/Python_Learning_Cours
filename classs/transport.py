class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        return f"{self.name} движется со скоростью {self.speed} км/ч"

    def get_info(self):
        return f"Транспорт: {self.name}"
