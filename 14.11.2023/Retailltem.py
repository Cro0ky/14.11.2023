from dataclasses import dataclass


@dataclass
class Retailltem:
    name: str
    discription: str
    kolvo: int
    price: float


item1 = Retailltem('Товар1', 'Пиджак', 12, 59.95)
item2 = Retailltem('Товар2', 'Дизайнерские джинсы', 40, 34.95)
item3 = Retailltem('Товар3', 'Рубажка', 20, 24.95)
print(item1)
print(item2)
print(item3)
