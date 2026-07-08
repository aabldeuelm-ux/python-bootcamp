print("==============================")
print("         PYTHON CAFE          ")
print("==============================")
print("\n         MENU")
print("\nCoffee        : ₹120")
print("Tea           : ₹80")
print("Sandwich      : ₹150")
print("Cake          : ₹90")
print("\n------------------------------")
customer_name = input("\nWhat is your name? ")
coffee = int(input("\nHow many coffee(s) would you like to have: "))
tea = int(input("How many cup(s) of tea would you like to have: "))
sandwich = int(input("How many sandwich(es) would you like to have: "))
cake = int(input("How many piece(s) of cake would you like to have: "))
coffee_price = float(120 * coffee)
tea_price = float(80  * tea)
sandwich_price = float(150 * sandwich)
cake_price = float(90 * cake)
subtotal = float(coffee_price + tea_price + sandwich_price + cake_price)
if subtotal == 0:
    print("\nYou have not ordered anything!")
else :
    gst = input("Would you like GST? (Y/N):")
    student = input("Are you a Student? (Y/N):")
    if gst == "Y":
        gst_amount = float(round(subtotal * 0.18 ,2))
        gst_addition = subtotal + gst_amount
    else:
        gst_amount = 0
        gst_addition = subtotal + gst_amount

    if student == "Y" and gst == "Y" :
        student_discount = round((gst_addition * 0.10), 2)
    elif student == "Y" and gst == "N":
        print("Student Discount is applicable only on GST bills.")
        student_discount = 0
    else:
        student_discount = 0

    final_bill = (subtotal + gst_amount) - student_discount

    print("==============================")
    print("         PYTHON CAFE          ")
    print("==============================")
    print(f"\nCustomer: {customer_name}")
    print(f"\nCoffee       x{coffee} : ₹{coffee_price}")
    print(f"Tea          x{tea} : ₹{tea_price}")
    print(f"Sandwich     x{sandwich} : ₹{sandwich_price}")
    print(f"Cake         x{cake} : ₹{cake_price}")
    print("\n-------------------------------")
    print(f"\nSubtotal        : ₹{subtotal}") 
    print(f"GST             : ₹{gst_amount}")
    print(f"Discount        : ₹{student_discount}")
    print("\n-------------------------------")
    print(f"\nFinal Bill      : ₹{final_bill}")
    if final_bill >= 1000:
        print("🎉 Congratulations!\nYou earned a FREE Brownie!")
    else:
        print("\nThank you for visiting!")