# Collect item names and prices
item1_name = input("Enter item 1 name: ")
item1_price = float(input("Enter item 1 price: "))

item2_name = input("Enter item 2 name: ")
item2_price = float(input("Enter item 2 price: "))

item3_name = input("Enter item 3 name: ")
item3_price = float(input("Enter item 3 price: "))

# Calculate total
total = item1_price + item2_price + item3_price

# Print formatted receipt
print("\n---------------------")
print(f"{item1_name:<15} ${item1_price:>5.2f}")
print(f"{item2_name:<15} ${item2_price:>5.2f}")
print(f"{item3_name:<15} ${item3_price:>5.2f}")
print("---------------------")
print(f"{'TOTAL':<15} ${total:>5.2f}")
