eye =  "blue"
eye = "green"
eye = "red"

def driveFoward():
    print("Drive forward")

def driveByColor():

    while(True):
        driveFoward()
        if(eye == "green"):
            turnRight()
        if(eye == "blue"):
            turnLeft()
        if (eye == "red"):
            # Stop here

