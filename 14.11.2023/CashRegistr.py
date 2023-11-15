from dataclasses import dataclass, field


@dataclass
class Retailltem:
    name: str
    discription: str
    kolvo: int
    price: float

    def __str__(self):
        return f'Имя - {self.name}\nОписание - {self.discription}\nkolvo - {self.kolvo}\nprice - {self.price}'


@dataclass
class CashRegister:
    item_list: list = field(default_factory=list)

    def purchase_item(self, purches):
        self.item_list.append(purches)

    def get_total(self):
        total_summ = 0
        for i in self.item_list:
            total_summ += i.price
        return total_summ

    def show_items(self):
        for i in self.item_list:
            print(i)

    def clear_register(self):
        self.item_list = []


cash_register = CashRegister()
item1 = Retailltem('Товар1', 'Пиджак', 12, 59.95)
item2 = Retailltem('Товар2', 'Дизайнерские джинсы', 40, 34.95)
item3 = Retailltem('Товар3', 'Рубажка', 20, 24.95)
# print(item1)
cash_register.purchase_item(item2)
cash_register.purchase_item(item1)
cash_register.show_items()
print(f'total: {cash_register.get_total()}')
cash_register.clear_register()
cash_register.show_items()