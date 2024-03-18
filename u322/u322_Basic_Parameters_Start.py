# Basic Parameters Start
def larger_val(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        print("The numbers are equal")
        return num2
    else:
        return num2

biggest_number = larger_val(14, 22)

print(biggest_number)