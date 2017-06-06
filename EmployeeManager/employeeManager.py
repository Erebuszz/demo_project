import employ
import pickle
from pathlib import Path

def main():

    add_exist = input("Load the existing list? (y for yes, n for no) ")
    # if the list exist, open it, else create a new one
    if(add_exist.lower() == 'y'):
        with open("inventory.pkl", 'rb') as the_file:
            the_item = pickle.load(the_file)
    else:
        the_item = employ.Inventory()

    manager(the_item)

def manager(the_item):

    while(True):
        print("\nMenu")
        print("-"*15)
        print("1. Look up a employee")
        print("2. Add a new employee")
        print("3. Change an existing employee")
        print("4. Delete a employee")
        print("5. List all")
        print("6. Quit the program")

        choice = int(input("Enter your choice: "))
        if(choice == 1):
            lookup_employee(the_item)
        elif(choice == 2):
            add_employee(the_item)
        elif(choice == 3):
            change_info(the_item)
        elif(choice == 4):
            delete_employee(the_item)
        elif(choice == 5):
            print(the_item)
        elif(choice == 6):
            break
        else:
            print("There is no such choice, try again~~~")

    save_file(the_item)

def lookup_employee(the_item):
    name_list = the_item.get_name_list()
    name = input("Enter the name: ")
    if(name in name_list):
        print("\nFound!")
    else:
        print("\nNot found!")

def add_employee(the_item):
    name_list = the_item.get_name_list()
    ID_list = the_item.get_ID_list()

    name = input("Name: ")
    if name in name_list:
        print("The name is already in the list!")
        return

    ID = int(input("ID: "))
    if ID in ID_list:
        print("This ID has already been used!")
        return

    Type = int(input("Type (1) Worker (2) Supervisor: "))
    if(Type == 1):
        shift = int(input("Shift: "))
        if(shift != 1 and shift != 2):
            print("This is not a choice (choose from 1 and 2)")
            return
        rate = float(input("Rate: "))
        the_item.add_item(name, employ.Worker(name, ID, shift, rate))
    elif(Type == 2):
        salary = float(input("Salary: "))
        bonus = float(input("Bonus: "))
        the_item.add_item(name, employ.Supervisor(name, ID, salary, bonus))
    else:
        print("Wrong type!")
        return

def change_info(the_item):
    name_list = the_item.get_name_list()
    name = input("Enter the name: ")

    if(name not in name_list):
        print("There is no such name!")
        return

    info = the_item.get_info(name)
    print("Current ID is", info.get_ID(), "enter a new ID: ", end='')
    new_ID = int(input())
    info.set_ID(new_ID)

    if(isinstance(info, employ.Worker)):
        print("Current shift is", info.get_shift(), "enter a new shift: ", end='')
        new_shift = int(input())
        if(new_shift != 1 and new_shift != 2):
            print("Only 1 or 2")
            return
        print("Current rate is", info.get_rate(), "enter a new rate: ", end='')
        new_rate = float(input())
        info.set_shift(new_shift)
        info.set_rate(new_rate)
    else:
        print("Current salary is", info.get_salary(), "enter a new salary: ", end='')
        new_salary = float(input())
        print("Current bonus is", info.get_bonus(), "enter a new bonus: ", end='')
        new_bonus = float(input())
        info.set_salary(new_bonus)
        info.set_bonus(new_bonus)
    print("Information updated!")

def delete_employee(the_item):
    name_list = the_item.get_name_list()
    name = input("Enter the name: ")

    if(name not in name_list):
        print("There is no such name!")
        return

    the_item.delete_item(name)
    print("Data deleted!")

def save_file(the_item):
    # save the list to the file
    save = input("Save the list? (y for yes, n for no) ")
    my_file = Path("inventory.pkl")
    overwrite = 'y'

    if(save.lower()=='y' and my_file.exists()):
        overwrite = input("File exists! Do you want to overwrite it? ")

    # if there is no existing file or you want to overwrite it, save the changes
    if(overwrite.lower() == 'y' or not my_file.exists):
            with open("inventory.pkl", "wb") as output:
                pickle.dump(the_item, output, pickle.HIGHEST_PROTOCOL)

main()