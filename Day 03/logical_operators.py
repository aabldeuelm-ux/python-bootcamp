# modulo operator %
# determine if the number is odd or even
print("ODD OR EVEN ?")
number = int(input("\nEnter a number: "))
remainder = number % 2
if remainder == 0:
    print(f"\nThe number {number} is an even number !")
else:
    print(f"\nThe number {number} is an odd number !")