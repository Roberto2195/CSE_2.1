total = 0.0
selected_a_sandwhich = True
selected_a_beverage= True
selected_french_fries = True
order = ["", "", "", 0]

sandwhich_index = 0
beverage_index = 1
fries_index = 2
ketchup_index = 3

order[sandwhich_index] = input("Would like a chicken, beef, or tofu sandwhich?")
if order[sandwhich_index] == "Chicken":
    total += 5.25
elif (selected_a_sandwhich[sandwhich_index] == "Beef:
    total += 6.25
else:
    print("Sorry, but that is not an available sandwhich.")
    selected_a_sandwhich = False
