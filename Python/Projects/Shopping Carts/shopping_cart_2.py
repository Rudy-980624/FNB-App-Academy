# shopping_cart_2.py

def display_cart(cart):
    if not cart:
        print("Your cart is currently empty.\n")
        return
    print("\n--- Current Shopping Cart ---")
    for i, (name, price) in enumerate(cart, start=1):
        print(f"{i}. {name} - R{price:.2f}")
    print()

def remove_item(cart):
    display_cart(cart)
    if not cart:
        return 0.0
    
    try:
        index = int(input("Enter the number of the item to remove: "))
        if 1 <= index <= len(cart):
            removed_item = cart.pop(index - 1)
            print(f"Removed '{removed_item[0]}' from the cart.\n")
            return removed_item[1]  # return price to subtract
        else:
            print("Invalid item number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
    return 0.0

def main():
    shopping_cart = []
    total_price = 0.0

    print("Welcome to the shopping cart!")
    print("Type the name of the item to add it.")
    print("Type 'remove' to delete an item.")
    print("Type 'done' to finish.\n")

    while True:
        user_input = input("Enter item name (or 'remove' / 'done'): ").strip()

        if user_input.lower() == 'done':
            break
        elif user_input.lower() == 'remove':
            removed_price = remove_item(shopping_cart)
            total_price -= removed_price
            continue

        try:
            item_price = float(input(f"Enter the price of '{user_input}': R"))
        except ValueError:
            print("Invalid price. Please enter a number.\n")
            continue

        shopping_cart.append((user_input, item_price))
        total_price += item_price

        print(f"Added '{user_input}' for R{item_price:.2f} to your cart.\n")

    print("\n--- Final Shopping Cart Summary ---")
    for i, (name, price) in enumerate(shopping_cart, start=1):
        print(f"{i}. {name} - R{price:.2f}")
    print(f"Total: R{total_price:.2f}")
    print("Thank you for shopping!")

if __name__ == "__main__":
    main()
