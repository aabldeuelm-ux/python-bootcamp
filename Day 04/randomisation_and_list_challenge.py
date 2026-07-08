import random
friends = ["Kambal", "Shaikhhh", "Saifuddin", "Dealer"]
#option 1
print(random.choice(friends))
#option 2
random_number = random.randint(0, len(friends) - 1 ) #length of the list is 4, so the index will be from 0 to 3, so we need to subtract 1 from the length of the list to get the last index
print(friends[random_number])
#option 3
cars = ["Ford", "BMW", "Volvo"]
random_number = random.randint(0, 2) # Generate a random integer between 0 and 2
print(cars[random_number])
    