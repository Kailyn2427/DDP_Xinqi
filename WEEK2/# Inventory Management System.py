# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
import string


inventory = {'coffee':2,'milk':3}

# Function to add an item to the inventory
def add_item(item, quantity:int):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.

    #if item in inventory:
    if item in inventory.keys():
        inventory[item] =inventory[item]+quantity#inventory[item] += quantity
    else:
        inventory.update({item:quantity})#inventory['item']=quantity
        print(f"{item} {quantity}(s) added to inventory.")
    pass

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
    #print(inventory.items())
    for item,quantity in inventory.items():
        print(f"{item}:{quantity}")
    pass

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity:int):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    inventory.update({item:quantity})
    pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.1
        if choice == "1":
            item = input("Enter the item you want to add: ")
            try:
              num = int(input("Enter the quantity you want to add: "))
            except ValueError:
              print("Error detected: You do not input a number\nError message:{e}")
              num=0

            add_item(item,num)
        elif choice == "2":
            view_inventory()
        elif choice == "3": 
            item = input("Enter the item you want to update: ")
            num = int(input("Enter the quantity you want to update: "))
            update_item(item, num)
        elif choice == "4":    
             #exit()
             break
        else:
            print("Invalid Input!")
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()

