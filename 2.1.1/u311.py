eye = "blue"
eye = "green"
eye = "red"
def driveFoward():
    print("Drive forward")
def turnRight():
    print("Turn right")
def turnLeft():
    print("Turn Left")
def driveByColor():
    while(True):
        driveFoward()
        if(eye == "green"):
            turnRight()
        if(eye == "blue"):
            turnLeft()
        if (eye == "red"):
            #Stop here
'''
Drive based on what color the robot sees
'''
def text_prompt():
    name = input("What is your name?")
    print("Hello" + name)
text_prompt()