def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            to_add = input("Enter the item to add: ")
            shopping_list.append(to_add)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            to_rm = input("What item do you want to remove?: ")
            if to_rm in shopping_list:
                shopping_list.remove(to_rm)
            else:
                print("Item not found.")
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

