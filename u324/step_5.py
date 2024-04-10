# this is a function definition
def assignment_1():
    print("Assignment 1 completed")
def assignment_2():
    print("Assignment 2 completed")

# this is a call of that function
assignment_1()
assignment_2_result = assignment_2()

# this function takes two arguments and returns their sum
def add(operand1, operand2):
    return operand1 + operand2


# since the add function returns a value it must be stored somewhere
sum = add(2, 3)
sum_2 = add(7, 4)
# that value isn't printed unless you use a print statement
print(sum)
print(sum_2)