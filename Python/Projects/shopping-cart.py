# shopping-cart.py

foods = []
prices = []
total = 0

while True:
    food = input(
        "Enter desired food or type 'quit' to quit: "
        )
    if food.lower() == "quit":
        break
    
    else:
        price = float(input(f"Enter price of {food}: R"))
        foods.append(food)
        prices.append(price)
        
print(" ----- Your Cart ----- ")

for food in foods:
    print(food)
    
for price in prices:
    total += price
    
print(f"Your total = R{total}")