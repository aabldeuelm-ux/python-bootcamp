print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? ₹"))
tip = float(input("How much would you like to tip, 10, 12 or 15 ? : "))
people = int(input("How many people will split the bill ? :"))
final_bill = (bill * ((tip / 100) + 1)) / people
print(f"The final amount that each person has to pay is: ₹{round(final_bill, 2)} ")