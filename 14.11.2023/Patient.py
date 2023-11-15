class Pateint:
    def __init__(self, fio, address, tel_num, sv_name, sv_tel_num):
        self.fio = fio
        self.address = address
        self.tel_num = tel_num
        self.sv_name = sv_name
        self.sv_tel_num = sv_tel_num

    def get_fio(self):
        print(self.fio)

    def get_address(self):
        print(self.address)

    def get_tel_num(self):
        print(self.tel_num)

    def get_sv_name(self):
        print(self.sv_name)

    def get_sv_tel_num(self):
        print(self.sv_tel_num)

    def set_fio(self, fio):
        self.fio = fio

    def set_address(self, address):
        self.address = address

    def set_tel_num(self, tel_num):
        self.tel_num = tel_num

    def set_sv_name(self, sv_name):
        self.sv_name = sv_name

    def set_sv_tel_num(self, sv_tel_num):
        self.sv_tel_num = sv_tel_num


class Procedure(Pateint):
    def __init__(self, nameProc, dateProc, doctor, price, fio, address, tel_num, sv_name, sv_tel_num,
                 proc_list=['Врачебный просмотр', 'Рентгеноскопия', 'Анализ крови']):
        super().__init__(fio, address, tel_num, sv_name, sv_tel_num)
        self.nameProc = nameProc
        self.dateProc = dateProc
        self.doctor = doctor
        self.price = price
        self.proc_list = proc_list

    def get_nameProc(self):
        print(self.nameProc)

    def get_date(self):
        print(self.dateProc)

    def get_doctor(self):
        print(self.doctor)

    def get_price(self):
        print(self.price)

    def set_name(self, nameProc):
        self.nameProc = nameProc

    def set_date(self, dateProc):
        self.dateProc = dateProc

    def set_doctor(self, doctor):
        self.doctor = doctor

    def set_price(self, price):
        self.price = price

    def get_proc_list(self):
        print(self.proc_list)

    def __str__(self):
        return f'''    Процедура:
Назание процедуры - {self.nameProc} 
Дата - {self.dateProc}
Врач - {self.doctor}
Стоимость процедуры - {self.price}
    Пациент:  
ФИО - {self.fio} 
Адресс - {self.address}
Телефон - {self.tel_num}' 
Имя для связи - {self.sv_name}
Телефон для связи - {self.sv_tel_num}

'''


procedur1 = Procedure('Врачебный просмотр', "Сегодняшняя", "Ирвин", 250.00, "Репнин Евгений Дмитриевич",
                      "Улица, Город, Область, индекс", 8971231321, "Имя для связи", 1231231223)
print(procedur1)
procedur2 = Procedure('Рентгеноскопия', "Сегодняшняя", "Джемисон", 500.00, "Имя Фамилия Отчетсво",
                      "Улица, Город, Область, индекс", 34567890, "Имя для связи1", 765435678)
print(procedur2)
procedur3 = Procedure('Анализ крови', "Сегодняшняя", "Смит", 200.00, "Имя1 Фамилия1 Отчество1",
                      "Улица, Город, Область, индекс", 456432456, "Имя для связи27", 56789765678)
print(procedur3)

procedur1.get_proc_list()
