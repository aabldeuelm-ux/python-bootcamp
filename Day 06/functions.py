def my_function():
    print("Hello user")
    user_input = input("Do you want to print the numbers from 1 - 100? Type 'y' or 'n'").lower()
    if user_input == "y":
        for i in range(1,101):
            print(i)
    elif user_input == "n":
        print("Okay bye!")

my_function()