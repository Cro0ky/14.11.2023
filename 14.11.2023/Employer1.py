class Employer:
    def __init__(self, name, id, departament, post):
        self.name = name
        self.id = id
        self.departament = departament
        self.post = post

    def set_name(self, name):
        self.name = name

    def set_deportament(self, departament):
        self.departament = departament

    def post(self, post):
        self.post = post

    def __str__(self):
        return f'{self.id}, {self.name}, {self.departament}, {self.post}'


def e_list(key, value, dict):
    dict[key] = value
    return dict


def e_search(dict, name):
    res = {}
    for key in dict:
        if name == dict[key].name:
            res = dict[key]
    if res:
        print(dict[key])
    else:
        print('Такого сотрудника нет!')


def e_change(name, departament, post, employee):
    employee.set_name()
    employee.set_deportament()
    employee.set_post()


def e_delete(key, dict):
    del dict[key]


counter = 0
reestr = {}

chel = Employer("Сбюзан Мейерс", 467899, "Бухгалтерия", "Вице-президент")
e_list(counter, chel, reestr)
counter += 1
chel2 = Employer("Марк Джоунс", 39110, "ИТ", "Программист")
e_list(counter, chel2, reestr)
counter += 2
chel3 = Employer("Джон Роджерс", 81774, "Производстсвенный", "Инженер")
e_list(counter, chel3, reestr)

e_search(reestr, "Джон Роджерс")
e_change('asdasdasdasd', 'adadda', 'xcvbnm', reestr[0])
print(reestr[0])
e_delete(0, reestr)
print(reestr[0])
