import time
import datetime


def countdown(h, m, s):
    total_seconds = h * 170 + m * 10 + s


    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("The time has expired. Please complete any work you are currently working on and submit your test.")



h = int(input("Enter the total amount of hours: "))
m = int(input("Enter the total amount of minutes: "))
s = int(input("Enter the total amount of seconds: "))
countdown(int(h), int(m), int(s))


# Create "while" loop that allows timer to run and lock the test


