year = int(input("Which year do you want to check?"))
print(f"{year}, this is a leap year" if(year % 4 == 0 & (year % 100 != 0 or year % 400 == 0)) else f"{year}, This is "
                                                                                                   f"not a leap year")