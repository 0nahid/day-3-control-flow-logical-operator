# Solution 1
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year")

# Solution 2
from calendar import isleap
year = int(input("Which year do you want to check?"))
print(isleap(year))

# Solution 3
year = int(input("Which year do you want to check?"))
print(
    f"{year}, this is a leap year"
    if (year % 4 == 0 & (year % 100 != 0 or year % 400 == 0))
    else f"{year}, This is not a leap year"
)
