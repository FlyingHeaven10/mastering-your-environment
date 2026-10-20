def print_menu():
    """Display the Taco Palace menu."""
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $4.00")
    print("3. Nachos - $3.50")
    print("4. Soft Drink - $1.45")
    print("5. Quit")


def get_price(selection):
    """Return the price of the selected food item."""
    if selection == 1:
        return 2.50
    elif selection == 2:
        return 4.00
    elif selection == 3:
        return 3.50
    elif selection == 4:
        return 1.45
    else:
        return 0.00


def get_item(selection):
    """Return the name of the selected food item."""
    if selection == 1:
        return "Taco"
    elif selection == 2:
        return "Burrito"
    elif selection == 3:
        return "Nachos"
    elif selection == 4:
        return "Soft Drink"
    else:
        return ""


def main():
    ordered_items = []
    total = 0.00

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    selection = 0

    while selection != 5:
        print_menu()

        try:
            selection = int(input("Enter your selection (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a whole number from 1 to 5.")
            continue

        if selection >= 1 and selection <= 4:
            item = get_item(selection)
            price = get_price(selection)

            print("You have selected a " + item + ".")
            ordered_items.append(item)
            total = total + price
        elif selection == 5:
            print("\nThank you for visiting Taco Palace!")
        else:
            print("Invalid selection. Please choose a number from 1 to 5.")

    print("\nYour order:")
    if len(ordered_items) == 0:
        print("You did not order any items.")
    else:
        for item in ordered_items:
            print("- " + item)

    print("Your total is $" + format(total, ".2f"))


if __name__ == "__main__":
    main()