"""Describe this function"""
def count_down():
    global number
    for number in range(11):
        print(number)
    return("Blast off!")


print(count_down())

name = input("What is your name?")
print(name)