print("Welcome to the rollercoster")
height = int(input("How tall are you in cm? "))
age = int(input("How old are you? "))
if height >= 180:
    print("You are tall enough to ride")
    if age >= 18:
        print("You've to purchase $12 ticket")
    else:
        print("You've to purchase $6 ticket")
else:
    print("You'll be able to ride when you're a little older")
