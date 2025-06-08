def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def get_numeric_choice():
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit():
            return int(choice)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = get_numeric_choice()

        if choice == 1:
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        elif choice == 2:
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
