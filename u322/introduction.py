@@ -1,5 +1,5 @@
import random

'''
########################## Basic user-generated function Start
def random_number():
    n1 = random.randint(30, 50)
@@ -13,14 +13,25 @@ def random_number():
    random_number()
    x += 1
import random
###################
####### Basic user-generated function End
########################## Basic user-generated function End
########################## Basic Parameters Start
'''
def larger_val(num1, num2):
    if num1 > num2:

        return num1
    elif num1 == num2:
        print("They are the same")
        return num2
    else:
        return num2


########################## Basic Parameters Start
biggest_number = larger_val(14, 22)

print(biggest_number)