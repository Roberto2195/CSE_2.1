cost = 0
selected_a_sandwhich = True
selected_a_beverage = True
selected_french_fries = True
order = []

food = input("Do you want, chicken $5.25, beef $6.25, tofu $5.75, or no food?")
if food == "chicken":
    order.append("chicken")
    cost += 5.25
elif (food == "beef"):
    order.append("beef")
    cost += 6.25
elif (food == "tofu"):
    order.append("tofu")
    cost += 5.75
else:
    print("You did not buy any food")
    order.append("no sandwhich")
    selected_a_sandwhich = False