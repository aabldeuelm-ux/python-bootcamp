print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island!\nYour mission is to find the hidden treasure.")
direction_choice = input('You\'re at a crossroad. Where do you want to go? Type Left or Right: ').lower()
if direction_choice == "left":
    wait_go = input("You came across a lake, do you want to wait for boat or swim across the lake? " \
    "Type boat or swim: ").lower()
    if wait_go == "boat":
        door_choice = input("Congratulations ! You came to the treasure island unharmed. " \
        "Choose a door between Red, Blue or Yellow: ").lower()
        if door_choice == "Blue":
            print("You are dead. You were eaten by the flying beasts!")
        elif door_choice == "Yellow":
            print("You win!.")
        else:
            print("Burned by fire!")
    elif wait_go == "swim":
        print("Game over!")
else:
    print("Game over! You were attacked by a trout.")

