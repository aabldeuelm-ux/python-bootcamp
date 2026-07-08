print("=============================================")
print("     Welcome to Python Pizza Deliveries!     ")
print("=============================================")
print("\n         MENU")
print("\nSmall Pizza       : ₹80")
print("Medimum Pizza     : ₹120")
print("Large Pizza       : ₹180")
print("Coke              : ₹50")
customer_name = input("What is your name?: ")
size = input("What size of pizza do you want? Small:S , medium:M, or large:L ? ").lower()
pepperoni = input("Do you want pepperoni on you pizza? (Y/N): ").lower()
cheese = input("Do you want extra cheese? (Y/N): ").lower()
coke = input("Do you want a can of coke? (Y/N): ").lower()
small_pizza = 80
medium_pizza = 120
large_pizza = 180
coke_price = 50
if size == "s":
    bill = 80
    pizza_size = "Small"
    if pepperoni == "y":
        bill += 10
    if cheese == "y":
        bill += 10
elif size == "m":
    bill = 120
    pizza_size = "Medium"
    if pepperoni == "y":
        bill += 20
    if cheese == "y":
        bill += 10
elif size == "l":
    bill = 180
    pizza_size = "Large"
    if pepperoni == "y":
        bill += 20
    if cheese == "y":
        bill += 10
if coke == "y":
    bill += 50
else:
    print("You haven't ordered anything !") 

print("==============================")
print("         PYTHON CAFE          ")
print("==============================")
print(f"\nCustomer: {customer_name}")
print(f"\nPizza Size - ₹{pizza_size} ")
print(f"Your final bill is: {bill}")
