sandwhich_type = ""
sandwhich_price = ""
fry_type = ""
beverage_type = ""
subtotal = 0.00
print("What type of sandwhich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwhich_type = input("Sandwhich Choice: ")
if sandwhich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwhich_type == "Tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25
print("Would you like a drink?")
if input("Yes")
    print("Small $1.00, Medium $1.75, Large $2.25")
if beverage_type == "Small":
    print("You chose small, which will be $1.00")
    subtotal += 1.00
print("Would you like to add fries?")
if input("Yes"):
    print("Small $1.00, medium $1.50, Large $2.00")
if fry_type == "Small":
    print("You chose small, which will be $1.00")
    subtotal += 1.00
elif fry_type == "Medium":
    print("You chose medium, which will be $1.50")
    subtotal += 1.50
else:
    print("You chose large, which will be $2.00")
    subtotal += 2.00