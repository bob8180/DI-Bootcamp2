menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}


def show_menu(menu_dict):
    if not menu_dict:  # Check if the dictionary is empty
        print("The menu is empty.")
        return
    
    for drink, price in menu_dict.items():
        print(f"{drink} - {price}₪")

show_menu(menu)


def add_item(menu_dict):
    drink = input("Enter drink name: ").strip()
    price = input("Enter price: ").strip()

    if not price.isdigit():
        print("Invalid price. Must be a number.")
        return

    if drink in menu_dict:
        print("Item already exists!")
        return

    menu_dict[drink] = int(price)
    print(f"{drink} added to the menu.")

# TEST CALL
menu = {}
add_item(menu)
print("Updated menu:", menu)

def update_price(menu_dict):
    drink = input("Enter the drink you want to update: ").strip()

    if drink not in menu_dict:
        print("Item not found.")
        return

    new_price = input("Enter the new price: ").strip()

    if not new_price.isdigit():
        print("Invalid price. Must be a number.")
        return

    menu_dict[drink] = int(new_price)
    print("Price updated!")

menu = {"Coffee": 10, "Tea": 8}

update_price(menu)

print(menu)

# D
def delete_item(menu_dict):
    drink = input("Enter the drink to delete: ").strip()

    if drink in menu_dict:
        del menu_dict[drink]
        print("Item deleted.")
    else:
        print("Item not found.")
menu = {"Coffee": 10, "Tea": 8}

delete_item(menu)

print(menu)

# E
def show_options():
    print("\n----- MENU OPTIONS -----")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")
    print("------------------------")

show_options()

# F
def run_coffee_shop():
    menu = {}

    while True:
        show_options()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_menu(menu)

        elif choice == "2":
            add_item(menu)

        elif choice == "3":
            update_price(menu)

        elif choice == "4":
            delete_item(menu)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

run_coffee_shop()


