import random
participants = ["Kambal", "Shaikhhh", "Saifuddin", "Dealer", "Ammmi"]
prizes = ["iPhone 14", "MacBook Pro", "iPad Pro", "Apple Watch", "AirPods Pro"]
print(participants)
start = input("Press Enter to start the lucky draw: ")
winners = int(input("How many winners do you want to select? "))
if winners > len(participants):
    print("Not enough participants to select that many winners.")
elif winners > len(prizes):
    print("Not enough prizes to select that many winners.")
else:
    for i in range(winners):
        prize_winner = random.choice(prizes)
        lucky_winner = random.choice(participants)
        print(f"Congratulations\nWinner :\n{lucky_winner}\nYou have won {prize_winner} in the lucky draw!")
        participants.remove(lucky_winner)  # Remove the winner from the list to avoid duplicate winners
        prizes.remove(prize_winner)  # Remove the prize from the list to avoid duplicate prizes
        print("---------------------------------------------")
