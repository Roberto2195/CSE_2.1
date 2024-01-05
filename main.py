"""Describe this function"""
def count_down():
    global number
    for number in range(11):
        print(number)
    return("Blast off!")


print(count_down())

name = input("What is your name?")
print(name)
print("You are awesome" + name)
len(name)

import random
number = random.randint(1,10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)
if guess == number:
    print("Correct!")
else:
    print("Sorry!" + "The number was" + str(number))

import math
radius = float(input("What is the radius of the tire?"))
seconds = float(input("What is the time in seconds?"))
circumference = (2 * math.pi * radius)
minutes = seconds / 60
remainder = seconds % 60
print("It traveled", int(minutes), "minutes and", remainder, "seconds")
print("The circumference of the tire is" + str(circumference))