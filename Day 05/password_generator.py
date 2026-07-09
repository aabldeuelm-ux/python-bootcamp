import random
letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '%', '&', '(', ')', '+', '=']
print("Welcome to PyPassword Generator!")
letters_choice = int(input("How many letters do you want in your password?: "))
numbers_choice = int(input("How many numbers do you want in your password?: "))
symbols_choice = int(input("How many symbols do you want in your password?: "))
password = []
for i in range(letters_choice):
    let = random.choice(letters)
    password.append(let)
for j in range(numbers_choice):
    num = random.choice(numbers)
    password.append(num)
for k in range(symbols_choice):
    sym = random.choice(symbols)
    password.append(sym)
    
random.shuffle(password)
final_password = "".join(password)
print(final_password)
