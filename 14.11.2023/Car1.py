from dataclasses import dataclass


@dataclass
class Car:
    _year_model: int
    _make: str
    _speed: int = 0

    def accelerate(self):
        self._speed += 5

    def Break(self):
        self._speed -= 5

    def get_speed(self):
        print(self._speed)


car = Car(2020, 'bmw', 100)

for i in range(5):
    car.accelerate()
    car.get_speed()
print(car)

for i in range(5):
    car.Break()
    car.get_speed()
print(car)
