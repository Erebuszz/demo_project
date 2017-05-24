import retail_item
import pickle
from pathlib import Path

def main():

    add_exist = input("Load the existing list? (y for yes, n for no) ")
    # if the list exist, open it, else create a new one
    if(add_exist.lower() == 'y'):
        the_file = open("inventory.pkl", 'rb')
        the_item = pickle.load(the_file)
        the_file.close()
        print(the_item)
    else:
        the_item = retail_item.Inventory()
    
    for_employee(the_item)

def for_employee(the_item):
    go_on = "y"

    # continue to import or not
    while(go_on.lower() == "y"):
        item = input("Enter the description of your items: ")
        units = int(input("Enter the units you want to store: "))
        item_dict = the_item.get_item_dict()
        
        # add the item to the stock
        if item in item_dict.values():
            # if the item exists, add the units to the existing stock
            key = list(item_dict.keys())[list(item_dict.values()).index(item)]
            the_item.item_in(key, units)
        else:
            # else create a new one
            price = float(input("Enter the price of your item: "))
            the_item.add_item(retail_item.RetailItem(item, units, price))

        print("Items stored!")
        go_on = input("continue? (y for yes, n for no) ")

    # save the list to the file
    save = input("Save the list? (y for yes, n for no) ")
    my_file = Path("inventory.pkl")
    overwrite = 'y'

    if(save.lower()=='y' and my_file.exists()):
        overwrite = input("File exists! Do you want to overwrite it? ")

    # if there is no existing file or you want to overwrite it, save the changes
    if(overwrite.lower() == 'y' or not my_file.exists):
            output = open("inventory.pkl", "wb")
            pickle.dump(the_item, output, pickle.HIGHEST_PROTOCOL)
            output.close()

main()