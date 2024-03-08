sandwhich_type = ""
sandwhich_price = ""
fry_type = ""
fry_size = ""
beverage_type = ""
beverage_size = ""
number_of_packets = ""
subtotal = 0.00

print("What type of sandwhich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwhich_type = input("Sandwhich Choice: ")
if sandwhich_type == "Chicken":
     print("You chose chicken, which will be $5.25")
     subtotal += 5.25
elif sandwhich_type == "Tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

print("Would you like a drink?")
if input("Yes or no?").lower() == "yes":
    print("Small $1.00, Medium $1.75, Large $2.25")
    beverage_size = input("What size drink?")

    if beverage_type == "Small":
        print("You chose small, which will be $1.00")
        subtotal += 1.00
    elif beverage_type == "Medium":
        print("You chose medium, which will be $1.75")
        subtotal += 1.75
    elif beverage_type == "Large":
        print("You chose large, which will be $2.25")
        subtotal += 2.25

print("Would you like to add fries?")
if input("Yes or no?").lower() == "yes":
    print("Small $1.00, medium $1.50, Large $2.00")
    fry_size = input("What size fry would you like?")

    if fry_type == "Small":
        print("You chose small, which will be $1.00")
        subtotal += 1.00
    elif fry_type == "Medium":
        print("You chose medium, which will be $1.50")
        subtotal += 1.50
    elif fry_type == "Large":
        print("You chose large, which will be $2.00")
        subtotal += 2.00

print("Would you like ketchup packets?")
if input("Yes or no?").lower() == "yes":
    number_of_packets = input("It 25 cents per packet. How many would you like?")
    subtotal += 0.25 * float(int(number_of_packets))
print("Your total is: ", subtotal)