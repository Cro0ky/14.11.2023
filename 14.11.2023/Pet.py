from dataclasses import dataclass


@dataclass
class Pet:
    __name: str
    __animal_type: str
    __age: str

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        print(self.__name)

    def get_animal_type(self):
        print(self.__animal_type)

    def get_age(self):
        print(self.__age)

    def input_data(self):
        self.__name = input('Введите имя: ')
        self.__animal_type = input('Введите тип животного: ')
        self.__age = int(input('Введите возраст: '))


pet = Pet('name', 'собака', 2)
pet.input_data()
print(pet.__dict__)