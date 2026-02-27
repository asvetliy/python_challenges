# Collect user details with appropriate casting
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_m = float(input("Enter your height in metres: "))
favourite_number = int(input("Enter your favourite number: "))

# Derived value: height in centimetres (cast to int)
height_cm = int(height_m * 100)

# Print formatted profile card
print("\n================================")
print("        YOUR PROFILE CARD")
print("================================")
print(f" Name:              {name}")
print(f" Age:               {age} years")
print(f" Height:            {height_m:.2f}m ({height_cm}cm)")
print(f" Favourite Number:  {favourite_number}")
print("================================")
