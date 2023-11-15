from dataclasses import dataclass


@dataclass
class Information:
    name: str
    address: str
    age: int
    tel_num: int

    def get_name(self):
        print(self.name)

    def get_address(self):
        print(self.address)

    def get_age(self):
        print(self.age)

    def get_tel_num(self):
        print(self.tel_num)

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_tel_num(self, tel_num):
        self.tel_num = tel_num


person1 = Information('name1', 'address1', 16, 89765432121)
person2 = Information('name2', 'address2', 15, 89545654345)
person3 = Information('name3', 'address3', 35, 89765678980)
print(person1)
print(person2)
print(person3)