# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.

from termcolor import colored, cprint


class InValid(Exception):
    pass


class Warehouse:
    def __init__(self):
        self.equipments = {
            "Printer": [Printer(3, 350, "Canon", True), Printer(1, 750, "Canon XL", False)],
            "Scanner": [Scanner(1, 239, "Brother 3902", True)],
            "Copy": [Copy(2, 153, "Epson Dynamic", "A5")]
        }

    def total(self):
        total_sum = 0
        for key_name in warehouse.equipments:
            total_sum += len(self.equipments[key_name])
        return total_sum

    def add_new(self, equip):
        if not equip.valid():
            raise InValid(colored("Error. The input is not correct", "yellow"))
        self.equipments[equip.__class__.__name__].append(equip)


class Equipment:
    def __init__(self, quantity, weight, model):
        self.quantity = quantity
        self.weight = weight
        self.model = model

    def __str__(self):
        return f"quantity:{self.quantity}, weight:{self.weight}, model:{self.model}"

    def valid(self):
        return self.quantity.isnumeric() and self.weight.isnumeric()


class Printer(Equipment):
    def __init__(self, quantity, weight, model, color):
        super().__init__(quantity, weight, model)
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, color:{self.color}"

    def valid(self):
        return super().valid() and (self.color == "True" or self.color == "False")


class Scanner(Equipment):
    def __init__(self, quantity, weight, model, double):
        super().__init__(quantity, weight, model)
        self.double = double

    def __str__(self):
        return f"{super().__str__()}, double:{self.double}"

    def valid(self):
        return super().valid() and (self.double == "True" or self.double == "False")


class Copy(Equipment):
    def __init__(self, quantity, weight, model, size):
        super().__init__(quantity, weight, model)
        self.size = size

    def __str__(self):
        return f"{super().__str__()}, size:{self.size}"

    def valid(self):
        return super().valid() and (self.size == "A4" or self.size == "A5" or self.size == "A6")


warehouse = Warehouse()

while True:
    cat_class = {1: Printer, 2: Scanner, 3: Copy}
    cat_attribute = {1: "Color (True or False)", 2: "Double (True or False)", 3: "Size(A4, A5, A6)"}

    choice = input("Choose from 1 to 4:\n1.Add product\n2.Show me the Warehouse\n3.How many equipment do we "
                   "have?\n4.Finish. \nYour choice: ")
    if choice == "1":
        try:
            choice_cat = int(input("1. Printer\n2. Scanner\n3. Copy\nВаш выбор: "))
        except ValueError:
            cprint("Error. Input is not correct", "yellow")
            continue
        quantity = (input("Quantity: "))
        weight = (input("Weight in gr: "))
        model = input("Model: ")
        attribute = input(f"{cat_attribute[choice_cat]}: ")
        new_equipment = cat_class[choice_cat](quantity, weight, model, attribute)
        try:
            warehouse.add_new(new_equipment)
        except InValid as err:
            print(err)
            continue
        cprint(f"New {cat_class[choice_cat].__name__} was added: {new_equipment}\n", "green")
    elif choice == "2":
        for key_name in warehouse.equipments:
            print(f"{key_name}:")
            for index, equipment in enumerate(warehouse.equipments[key_name]):
                cprint(f"ID: {index + 1}, {equipment}\n{'-' * 15}", "blue")
    elif choice == "3":
        for key_name in warehouse.equipments:
            cprint(f"{key_name} -> {len(warehouse.equipments[key_name])}\n{'-' * 15}", "blue")
        cprint(f"TOTAL -> {warehouse.total()}\n{'-' * 15}", "blue", attrs=['bold'])
    elif choice == "4":
        cprint("The end.", attrs=['underline'])
        break
    else:
        cprint("Error. Input is not correct", "yellow")
