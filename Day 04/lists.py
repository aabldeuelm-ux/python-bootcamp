fruits = ["Apple", "Peach", "Pear"]
print(fruits[0]) # Apple
print(fruits[1]) # Peach    
print(fruits[2]) # Pear
print(fruits[-1]) # Pear starts from the end of the list
fruits.insert(1, "Banana") # Insert Banana at index 1
print(fruits) # ['Apple', 'Banana', 'Peach', 'Pear']
fruits.remove("Banana") # Remove Banana from the list
print(fruits) # ['Apple', 'Peach', 'Pear']
fruits.append("Mango") # Add Mango to the end of the list
fruits.pop(1) # Remove the item at index 1 (Peach)
print(fruits) # ['Apple', 'Pear', 'Mango']
fruits[1] = "Blueberry" # Change the item at index 1 to Blueberry
print(fruits) # ['Apple', 'Blueberry', 'Mango']
# fruits.clear() # Clear the list
# print(fruits) # []
cars = ["Ford", "BMW", "Volvo"]
cars.append("Toyota") # Add Toyota to the end of the list
cars[0] = "Mercedes" # Change the item at index 0 to Mercedes
cars.pop(2) # Remove the item at index 2 (Volvo)
print(cars) # ['Mercedes', 'BMW', 'Toyota']
cars.insert(1, "Audi") # Insert Audi at index 1
print(cars.index("BMW")) # Get the index of BMW

lists = [cars, fruits] # Create a list of lists 
print(lists) # [['Mercedes', 'Audi', 'BMW', 'Toyota'], []]
print(cars[1]) # Audi
print(cars[2]) # BMW    
print(lists[0]) # Audi
print(lists[1]) # []
print(lists[1][0]) # Audi
