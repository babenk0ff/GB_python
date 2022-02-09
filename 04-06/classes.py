from abc import ABC, abstractmethod


class WarehouseError(Exception):
    def __init__(self):
        self.message = None

    def __str__(self):
        return self.message


class IsNotIntWarehouse(WarehouseError):
    def __init__(self, message='Значение не типа int'):
        self.message = message


class IsNotStrWarehouse(WarehouseError):
    def __init__(self, message='Значение не типа str'):
        self.message = message


class IsNotOfficeEquipmentWarehouse(WarehouseError):
    def __init__(self, message='Объект не является типом OfficeEquipment'):
        self.message = message


class OfficeEquipment(ABC):
    @abstractmethod
    def __init__(self, vendor, model, serial_num, year):
        self.type = self.__class__.__name__
        self.vendor = vendor
        self.model = model
        self.serial_num = serial_num
        self.year = year

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, vendor, model, serial_num, year, is_laser=True):
        super().__init__(vendor, model, serial_num, year)
        self.laser = is_laser

    def __str__(self):
        return str(self.__dict__)


class Scanner(OfficeEquipment):
    def __init__(self, vendor, model, serial_num, year, paper_size):
        super().__init__(vendor, model, serial_num, year)
        self.paper_size = paper_size

    def __str__(self):
        return str(self.__dict__)


class Copier(OfficeEquipment):
    def __init__(self, vendor, model, serial_num, year, is_bw=True):
        super().__init__(vendor, model, serial_num, year)
        self.is_bw = is_bw

    def __str__(self):
        return str(self.__dict__)


class Warehouse:
    def __init__(self, company, address):
        self.company = company
        self.address = address
        self.__equipment_list = []

    def take_equipment(self, item: OfficeEquipment, amount: int):
        """Приём техники на склад в количестве 'amount'"""
        self.check_type_equipment(item)
        self.check_type_int(amount)
        index = self.if_exist(item)
        if index is not None:
            self.__equipment_list[index][1] += amount
        else:
            self.__equipment_list.append([item, amount])

    def export_equipment(self, item, amount, dst_address):
        """Отправка техники в количестве 'amount' со склада на адрес 'dst_address'"""
        self.check_type_int(amount)
        index = self.if_exist(item)
        if index is not None:
            target = self.__equipment_list[index]
            if target[1] < amount:
                print(f'Для отправки не хватает {amount - target[1]} шт (на складе {target[1]} шт)')
            elif target[1] >= amount:
                target[1] -= amount
                if target[1] == 0:
                    target.remove()
                print(
                    f'{item.type} в количестве {amount} шт '
                    f'был отправлен в отделение компании {self.company} '
                    f'по адресу {dst_address}'
                )
        else:
            print('Такого оборудования нет на складе')

    def show_warehouse_info(self):
        print(
            f'Компания: {self.company}\n'
            f'Адрес склада: {self.address}'
        )

    def show_equipment_info(self):
        """Отображение подробной информации о технике на складе"""
        if len(self.__equipment_list) != 0:
            print('Содержимое склада:')
            for item in self.__equipment_list:
                for k, v in item[0].__dict__.items():
                    print(f'{k}: {v}')
                print(f'Количество: {item[1]}\n')
        else:
            print('Склад пуст')

    def show_amount_equipment(self, item_type):
        """Показ количества техники типа item_type"""
        self.check_type_str(item_type)
        amount = sum(
            [item[1] for item
             in self.__equipment_list
             if item[0].__dict__['type'] == item_type.capitalize()]
        )
        if amount > 0:
            print(f'Количество оргтехники типа {item_type.capitalize()} на складе: {amount} шт')
        else:
            print(f'Оргтехники типа {item_type.capitalize()} на складе нет')

    def if_int(self, val):
        pass

    def if_exist(self, item):
        for i, val in enumerate(self.__equipment_list):
            if item == val[0]:
                return i
        return None

    @staticmethod
    def check_type_int(value):
        if type(value) != int:
            raise IsNotIntWarehouse

    @staticmethod
    def check_type_str(value):
        if type(value) != str:
            raise IsNotIntWarehouse

    @staticmethod
    def check_type_equipment(obj):
        if not isinstance(obj, OfficeEquipment):
            raise IsNotOfficeEquipmentWarehouse



