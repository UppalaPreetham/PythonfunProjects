height = int(input("what is your height? \n"))
age = int(input("what is your age? \n"))
photo = input("Do you need photo? say 'yes/no'")
if height >= 120:
    if age <= 8:
        if photo == "yes":
            print("your ticket is 8$")
        else:
            print("your ticket is 5$")
    elif age <= 18:
        if photo == "yes":
            print("your ticket is 13$")
        else:
            print("your ticket is 10$")
    elif photo == "yes":
        print("your ticket is 21$")
    else:
        print("your ticket is 18$")
else:
    print("you are not eligible for adventure")