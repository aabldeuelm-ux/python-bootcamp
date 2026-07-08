print("==============================")
print("   Thieves Bank Association   ")
print("==============================")
customer_name = input("\nEnter customer name: ")
previous_balance = 10000.00
withdrawal_amt = float(input("Enter the amount you would like to withdraw: "))
print("\n==============================")
print("       Transaction Status       ")
print("==============================")
print(f"\nCustomer Name      : {customer_name}")
print(f"\nPrevious Balance   : ₹{round(previous_balance, 2)}")
print(f"Withdrawal Amount  : ₹{round(withdrawal_amt, 2)}")
if withdrawal_amt <= previous_balance:
    remaining_balance = (previous_balance - withdrawal_amt)
    print(f"Remaining Balance  : ₹{round(remaining_balance, 2)}")
    print("\nTransaction Status : SUCCESS ")
    print("Thankyou for theivery with us!")
else:
    print("Withdrawal amount is greater than the current balance in your account ")
    print("\nTransaction Status : FAILED")
    print("Better Rob something and then come back !")

