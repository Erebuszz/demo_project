import retail_item
import pickle
from pathlib import Path

def main():
    # open thte inventory
    the_file = open("inventory.pkl", 'rb')
    the_item = pickle.load(the_file)
    the_file.close()
    # make a shopping list
    the_purchase = retail_item.CashRegister()
    
    for_customer(the_item, the_purchase)

def for_customer(the_item, the_purchase):
    temp_list = {}

    while (True):
        print(the_item)
        choice = input("enter merchandise number to purchase, z to clear cash register, or x to check out item list: ")
        
        # see if the choice is within the item list
        if(choice.isdigit() and 1 <= int(choice) <= len(the_item.get_item_dict())):
            choice = int(choice)
            num = int(input("How many would you like to buy? "))
            unit_in_stock = the_item.get_units(choice)
            price = the_item.get_price(choice)
            description = the_item.get_description(choice)

            # see if the customer has bought a couple of this item before
            if description in temp_list:
                purchaseNum = num + the_purchase.get_num(description)
            else:
                purchaseNum = num

            # see if there is enough remains for customer to buy
            if(unit_in_stock < purchaseNum):
                    print("Sorry! There aren't that much in stock!")
            else:
                    the_purchase.purchase_item(description, num, price)
                    temp_list[description] = choice

        # clear the shopping list
        elif(choice.lower() == 'z'):
            temp_list.clear()
            the_purchase.clear()
        
        # check out the purchase
        elif(choice.lower() == 'x'):

            # make changes to the stock
            for key, order in temp_list.items():
                num = the_purchase.get_num(key)
                the_item.item_out(order, num)
            
            # save the stock changes
            output = open("inventory.pkl", "wb")
            pickle.dump(the_item, output, pickle.HIGHEST_PROTOCOL)
            output.close()
            
            print(the_purchase)
            print(the_item)
            break
        
        else:
            print("There is no such choice! Try again!")

main()