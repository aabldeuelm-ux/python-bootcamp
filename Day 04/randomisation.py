import random
# a = random.randint(1, 10) # Generate a random integer between 1 and 10
# print("Random number generated is:", a)

# random_float = random.random() * 10 # Generate a random float between 0 and 10
# print(random_float) 

# random_float_1 = random.uniform(1,10) # Generate a random float between 1 and 10
# print(random_float_1)

toss = input("Type T to toss the coin: ").lower()
if toss == "t":
    coin = random.randint(0, 1)
    if coin == 0:
        print("Heads.")
    else:
        print("Tails.")
