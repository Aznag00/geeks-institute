from menu_item import MenuItem , MenuManager

def show_user_menu():
    while True:
        print("\nProgram Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("X - Exit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'X':
            show_restaurant_menu()
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ").strip()
    
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def update_item_from_menu():
    old_name = input("Enter the current name of the item: ").strip()
    
    item = MenuManager.get_by_name(old_name)
    if item:
        new_name = input("Enter the new name: ").strip()
        new_price = float(input("Enter the new price: "))
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Error: Item not found.")

def view_item():
    name = input("Enter the name of the item to view: ").strip()
    
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item found: {item.item_name}, Price: {item.item_price}")
    else:
        print("Item not found.")

def show_restaurant_menu():
    print("\nRestaurant Menu:")
    items = MenuManager.all_items()
    for item in items:
        print(f"{item.item_name}: ${item.item_price}")

if __name__ == "__main__":
    show_user_menu()