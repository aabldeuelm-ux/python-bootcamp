print("==================================")
print("        CINEMATIC UNIVERSE        ")
print("==================================")
print("\nWelcome to Cineverse!")
name = input("\nWhat is your name? ")
age = int(input("What is your age? "))
popcorn = input("Would you like popcorn? (Y/N):")
if age<12 :
    ticket_price = 150
elif age >=12 and age<18:
    ticket_price = 220
else :
    ticket_price = 350
if popcorn==str("Y") :
    popcorn_quantity = int(input("How many popcorn tubs would you like to have? :"))
    popcorn_price = 120 * popcorn_quantity
else :
    popcorn_price = 0

total_bill = ticket_price + popcorn_price
print(f"\nHello, {name}!")
print(f"\nMovie Ticket : {ticket_price}")
print(f"Popcorn      : {popcorn_price}")
print("----------------------")
print(f"Total Bill   : {total_bill}")
print("----------------------")
if total_bill > 500 :
    print("🎉 Congratulations!\nYou have earned a FREE soft drink!")
else :
    print("Enjoy your movie!")