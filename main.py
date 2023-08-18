#Author - Prashanth.G

import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
word = list("_" * len(chosen_word))
lives = 6
while lives > 0:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in chosen_word:
        if guess in word:
            print(f"You have already guessed {guess}")
        else:
            letter_index = 0
            for letter in list(chosen_word):
                if letter == guess:
                    word[letter_index] = letter
                letter_index += 1
            print("".join(word))
            if chosen_word == "".join(word):
                break
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])

if chosen_word == "".join(word):
    print("You won!")
else:
    print("You lose")
