height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight / (height ** 2), 2)
a = "underweight"
b = "normal weight"
c = "over weight"
d = "obese"
e = "extremely obese"
x = f"Your bmi is {bmi}"
y = f"you are"
z = f"{x} & {y} "
print(f"{z}{a}" if bmi < 18.5 else f"{z}{b}" if bmi < 25 else f"{z}{c}" if bmi <30 else f"{z}{d}" if bmi < 35 else f"{z}{e}")