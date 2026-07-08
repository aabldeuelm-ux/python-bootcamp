import random
print('''
=================================================
          PYTHON CINEMA
=================================================

Now Showing                  Prices

1. Superman                  : 250
2. F1                        : 300
3. Jurassic World            : 280
4. How to Train Your Dragon  : 220          
5. Fantastic Four            : 380
''')

movies = ["Superman", "F1", "Jurassic World", "How to Train Your Dragon", "Fantastic Four"]
prices = [250, 300, 280, 220, 380]
seat_types = ["Silver", "Gold", "Platinum"]
seat_prices = [0, 100, 250]
seat_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
pop_quantity = 0
popcorn_price = 0
coke_quantity = 0
coke_price = 0
discount = 0
seat_choice = 0
screen = ["Screen 1", "Screen 2", "Screen 3"]
username = input("What is your name ?: ")
user_choice = int(input("Enter your choice of movie 1-5: "))
movie_index = user_choice - 1
number_movies = len(movies)
if movie_index < 0 or movie_index >= number_movies:
    print("Invalid choice. Please choose again!")
else:
    tickets = int(input("How many tickets do you want? :"))
    if tickets > 0:
        seat_choice = int(input('''Which type of seat do you prefer ?
\nSeat Type           Prices
\n1. Silver.          ₹0
2. Gold.            ₹100
3. Platinum.        ₹250
                                
'''))
        seat_index = seat_choice - 1
        if seat_index < 0 or seat_index >= len(seat_types):
            print("Invalid seat type. Please choose again!")
        else:
            seat_number_allocation = random.choice(seat_number)
            assign_screen = random.choice(screen)
            booking_id = random.randint(200, 450)
            subtotal = prices[movie_index] * tickets + seat_prices[seat_index] * tickets
        popcorn = input("Fancy a popcorn? (Y/N): ").lower()
        if popcorn == "y":
            pop_quantity = int(input("How many popcorn buckets?: "))
            if pop_quantity > 0:
                popcorn_price = 150 * pop_quantity
        elif popcorn == "n":
            popcorn_price = 0
        else:
            popcorn_price = 0
            print("Please enter y or n.")
        coke = input("Want a coke? (Y/N)").lower()
        if coke == "y":
            coke_quantity = int(input("How many cans of coke?: "))
            if coke_quantity > 0:
                coke_price = 80 * coke_quantity
        elif coke == "n":
            coke_price = 0
        else:
            coke_price = 0
            print("Please enter y or n.")
        final_bill = subtotal + popcorn_price + coke_price
        student_discount = input("Are you a student? (Y/N)").lower()
        if student_discount == "y":
            discount = final_bill * 0.10
            final_bill -= discount
        elif student_discount == "n":
            discount = 0
        else:
            print("Please enter y or n.")
            
        print(f''' ====================================

Customer:        {username}

Movie:           {movies[movie_index]}

--------------------------------------------------

                Quantity/Type               Price

Booking ID:      {booking_id}

Seat number:     {seat_number_allocation}

Screen:          {assign_screen}

Seat Type       {seat_types[seat_index]}                      ₹{seat_prices[seat_index]}

Tickets         {tickets}                            ₹{prices[movie_index] * tickets}

--------------------------------------------------

Subtotal                                    ₹{subtotal}

--------------------------------------------------

Popcorn         {pop_quantity}                            ₹{popcorn_price}

Coke            {coke_quantity}                            ₹{coke_price}

Discount                                    ₹{discount}

--------------------------------------------------

Final Bill                                  ₹{final_bill}

====================================
''')   

    else:
        print("Invalid ticket count. Select atleast one ticket.")
