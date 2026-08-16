import random
import hangman_art
import hangman_words
print(hangman_art.logo)
words = hangman_words.word_list
chosen_word = random.choice(words).lower()
lives = 6
print(chosen_word)
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess the word: ").lower()
    display = ""
    if guess in correct_letters:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        continue
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter) 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    print(hangman_art.stages[lives])

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(f"You have {lives} lives remaining.")
        print(hangman_art.stages[lives])
        if lives == 0:
            game_over = True
            print("You lose! The word was:", chosen_word)
    if "_" not in display:
        game_over = True
        print("**********************You win!**********************")
        print(f"Congratulations! You've guessed the word correctly.The word was {chosen_word} ")