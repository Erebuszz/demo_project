class RetailItem:

    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price

class Inventory:

    def __init__(self):
        self.__items = {}

    def get_description(self, order):
        return self.__items[order].description

    def get_units(self, order):
        return self.__items[order].units

    def get_price(self, order):
        return self.__items[order].price

    # get a dictionary of order:description of the existing items
    def get_item_dict(self):
        item_dict = {}     
        for i in range(1, len(self.__items)+1):
            item_dict[i] = self.__items[i].description
        return item_dict

    def add_item(self, item):
        order = len(self.__items) + 1
        self.__items[order] = item
    
    def remove_item(self, order):
        self.__items.pop(order, None)   # delete the item
        # move the order of the items behind it forward
        for i in range(order+1, len(self.__items)+1):
            self.__items[i-1] = self.__items.pop(i, None)

    def item_in(self, order, num):
        self.__items[order].units += num

    def item_out(self, order, num):
        self.__items[order].units -= num

    def __str__(self):
        out = "no\t\tDescription\tUnits in Inventory\tPrice"
        for key, item in self.__items.items():
            temp = "%-2d\t%19s\t%18d\t%5.2f" % (key, item.description, item.units, item.price)
            out += '\n' + temp
        return out

class CashRegister:

    def __init__(self):
        self.__list = {}
        self.__sum = 0

    def purchase_item(self, descript, num, price):
        try:
            self.__list[descript] += num
        except KeyError:
            self.__list[descript] = num
        self.__sum += num * price

    def get_num(self, descript):
        return self.__list[descript]

    def __str__(self):
        out = ""
        for key, num in self.__list.items():
            out += "%-15s\tquantity:%3d\n" % (key, num)
        out += "Total price: %.2f\n" % (self.__sum)
        return out
    
    def clear(self):
        self.__list.clear()
        self.__sum = 0