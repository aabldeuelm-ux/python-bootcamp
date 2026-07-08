# print("Welcome to Roller Coaster Ride !!")
# height = int(input("\nWhat is you height? "))
# age = int(input("What is your age?"))
# # if height >= 120:
# #     print("Enjoy your ride !\nYou are taller than the most shawtiisss !!")
# #     if age < 12:
# #         print("Please pay $5.") 
# #     elif age <= 18:
# #         print("Please pay $7.")
# #     else:
# #         print("Please pay $12.")
# # else:
# #     print("Shawtyyyy!")

print("Welcome to Roller Coaster Ride !!")
height = int(input("\nWhat is your height? "))
age = int(input("What is your age?"))

if height >= 120:
    print("You are taller than the most shawtiisss !!")
    if  45 <= age <= 55:
        bill = "Free"
    elif age <= 12:
        bill = 50
        print("Child tickets are ₹50.") 
    elif age <= 18:
        bill = 70
        print("Teen tickets are ₹70.")
    else:
        bill = 120
        print("Adult tickets are ₹120.")
    
    photos = input("Do you want to have photos taken of your ride? (Y/N)")
    if photos == "Y" and  age < 45:
        bill += 30
        print("Enjoy your ride !")
    elif photos == "Y" and 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
    
    print(f"Your Total bill is ₹{bill}")
else:
    print("Shawtyyyy!")

# if age >= 45 and age <= 55:
#     print("You can ride for free")