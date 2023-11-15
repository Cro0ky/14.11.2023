from dataclasses import dataclass, field


@dataclass
class Employer:
    name: list = field(default_factory=list)
    id: list = field(default_factory=list)
    department: list = field(default_factory=list)
    post: list = field(default_factory=list)

    # def set_name(self):
    #     self.name =
    #
    # def set_id(self):
    #     self.name =
    #
    # def set_drpartament(self):
    #     # self.name = post
    #
    # def set_post(self):
    #     self.post = post

    def tabl(self):
        print('     ИМЯ')
        for i in self.name:
            j = len(i)
            print(' ', '-' * j)
            print(f'| {i} |')
            print(' ', '-' * j)

        print('     ID')
        for i in self.id:
            num = len(i)
            print(' ', '-' * num)
            print(f'| {i} |')
            print(' ', '-' * num)


        print('     ОТДЕЛ')
        for i in self.department:
            a = len(i)
            print(' ', '-' * a)
            print(f'| {i} |')
            print(' ', '-' * a)

        print('     ДОЛЖНОСТЬ')
        for i in self.post:
            ja = len(i)
            print(' ', '-' * ja)
            print(f'| {i} |')
            print(' ', '-' * ja)


emp1 = Employer(["Сбюзан Мейерс", "Марк Джоунс", "Джон Роджерс"],
                ['467899', '39119', '81774'],
                ["Бухгалтерия", "ИТ", "Производстсвенный"],
                ["Вице-президент", "Программист", "Инженер"],)
emp1.tabl()
