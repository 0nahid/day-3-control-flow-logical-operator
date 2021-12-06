height = int(input("Enter your height in cm:"))
age = int(input("Enter your age:"))
x= "You can buy a ticket & You've to pay";
print(f"{x} $12 " if (height >= 120 & age >= 18) else f"{x} 9$" if(age <= 12) else f"{x} 15$" if(age > 22) else "You've to pay 0$")