class Employee:
    def __init__(self, name, ID):
        self.__name = name
        self.__ID = ID

    def set_ID(self, ID):
        self.__ID = ID

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

class Worker(Employee):
    def __init__(self, name, ID, shift, rate):
        Employee.__init__(self, name, ID)

        self.__shift = shift
        self.__rate = rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_rate(self, rate):
        self.__rate = rate

    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate

class Supervisor(Employee):
    def __init__(self, name, ID, salary, bonus):
        Employee.__init__(self, name, ID)

        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary
    
    def set_bonus(self, bonus):
        self.__bonus = bonus
    
    def get_salary(self):
        return self.__salary
    
    def get_bonus(self):
        return self.__bonus

class Inventory:
    def __init__(self):
        self.__items = {}

    def add_item(self, name, item):
        self.__items[name] = item

    def delete_item(self, name):
        self.__items.pop(name)

    def get_name_list(self):
        item_list = []
        for name in list(self.__items.keys()):
            item_list.append(name)
        return item_list

    def get_ID_list(self):
        item_list = []
        for item in self.__items.values():
            item_list.append(item.get_ID())
        return item_list

    def get_info(self, name):
        return self.__items[name]

    def __str__(self):
        out = "\n"+ "-"*15 + "\n"
        for item in self.__items.values():
            if(isinstance(item, Worker)):
                out += ("W- Name: %s, ID: %d, Shift: %d, Rate: %.2f\n" % (item.get_name(), item.get_ID(), item.get_shift(), item.get_rate()))
            else:
                out += ("S- Name: %s, ID: %d, Salary: %.2f, Bonus: %.2f\n" % (item.get_name(), item.get_ID(), item.get_salary(), item.get_bonus()))
            out += "-"*15 + "\n"
        return out