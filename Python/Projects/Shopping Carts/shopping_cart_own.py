# shopping_cart_own.py

def main():
    shopping_cart = []
    total_price = 0.0

    print("Welcome to your shopping cart!")
    
    while True:
        item_name = input("Enter the name of the item (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break

        try:
            item_price = float(input(f"Enter the price of '{item_name}': R"))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        shopping_cart.append((item_name, item_price))
        total_price += item_price

        print(f"Added '{item_name}' for R{item_price:.2f} to your cart.\n")

    print("\n--- Shopping Cart Summary ---")
    for i, (name, price) in enumerate(shopping_cart, start=1):
        print(f"{i}. {name} - R{price:.2f}")

    print(f"Total: R{total_price:.2f}")
    print("Thank you for shopping!")

if __name__ == "__main__":
    main()
