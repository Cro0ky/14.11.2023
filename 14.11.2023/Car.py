from dataclasses import dataclass


@dataclass
class MyCar:

    def go(self):
        return 'go'


my_car = MyCar()
print(my_car.go())
