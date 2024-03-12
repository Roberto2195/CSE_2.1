customer_order = ["Fries", "Shake"]
item = input("What else would you like to order? ")
customer_order.append(item)

print("You ordered", customer_order)
answer = input("Is your order correct? ")
if (answer == "yes"):
  print("Great! Your order is coming right up!")
else:
  print("Okay, I will remove", item, "from your order.")
  customer_order.remove(item)

print("Your new order is", customer_order)