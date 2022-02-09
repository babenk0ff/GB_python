from classes import *

warehouse = Warehouse('Intel', 'NY, Main st, 21')

printer_1 = Printer('HP', 1001, 'asdFh-20', 2020)
printer_2 = Printer('Brother', 'br-123', '3472-548', 2019)
xerox_1 = Copier('Xerox', '233-dd', 3593373, 2010)
scanner_1 = Scanner('HP', 'scan-jet100', '248dh2', 2017, 'A3')

warehouse.take_equipment(printer_1, 10)
warehouse.take_equipment(printer_1, 5)
warehouse.take_equipment(xerox_1, 13)
warehouse.take_equipment(scanner_1, 5)
warehouse.show_equipment_info()

warehouse.export_equipment(xerox_1, 5, 'Boston, 23 Awe')

warehouse.export_equipment(printer_1, 100, 'Boston, 23 Awe')

warehouse.show_amount_equipment('Printer')
