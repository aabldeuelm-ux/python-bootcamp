print("==============================")
print("     PYTHON SHOPPING MALL     ")
print("==============================")
print("\nMENU")
print("Laptop_Bag = ₹1500")
print("Headphones = ₹2500")
print("Keyboard   = ₹1200")
print("Mouse      = ₹700")
name = input("What is your name? ")
print(type(name))
print("How many of each items do you want?")
laptop_bag = int(input("Laptop Bag: "))
headphones = int(input("Headphones: "))
keyboard = int(input("Keyboards: "))
mouse = int(input("Mouse: "))
laptop_price = (1500 * laptop_bag)
headphone_price = (2500 * headphones)
keyboard_price = (1200 * keyboard)
mouse_price = (700 * mouse)
subtotal = (laptop_price + keyboard_price + headphone_price + mouse_price)
student = input("Are you student? (Y/N): ")
if student == "Y":
    discount = subtotal * 0.10
else:
    discount = 0
gst = input("Would you like gst? (Y/N): ")
if gst == "Y":
    gst_amount = subtotal * 0.18
else:
    gst_amount = 0
delivery = input("Would you like Home delivery? (Y/N): ")
if delivery == "Y":
    delivery_charge = 80
else:
    delivery_charge = 0
final_bill = subtotal + gst_amount + delivery_charge - discount 
print(f"\nYour final bill is : ₹{round(final_bill, 2)}")
while(True):
    amount_paid = int(input("How much cash are you paying? "))
    if amount_paid < final_bill:
        print("Insufficient Payment!")
    else:
        change = amount_paid - final_bill
        print("==============================")
        print("   PYTHON SHOPPING RECIEPT    ")
        print("==============================")
        print(f"\nCustomer name : {name}")
        print(f"\nLaptop_Bag   x{laptop_bag}    ₹{laptop_price}")
        print(f"Headphones   x{headphones}      ₹{headphone_price}")
        print(f"Keyboard     x{keyboard}    ₹{keyboard_price}")
        print(f"Mouse        x{mouse}    ₹{mouse_price}")
        print("\n------------------------------")
        print(f"\nSubtotal       ₹{subtotal}")
        print(f"GST            ₹{gst_amount}")
        print(f"Discount       ₹{discount}")
        print(f"Delivery       ₹{delivery_charge}")
        print("\n------------------------------")
        print(f"\nFinal Bill          ₹{final_bill}")
        print(f"Cash Paid           ₹{amount_paid}")
        print(f"Change              ₹{change}")
        break