# 100 Days of Code Practice Project
# Hangman game

# Import wordlist and ascii art
import random
from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# Game logic
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
      print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

  
    if guess not in chosen_word:
      print(f"{guess} is not in this word")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word was '{chosen_word}'")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])