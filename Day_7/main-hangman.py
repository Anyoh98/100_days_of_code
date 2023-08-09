from Hangman_art import logo
import random

from Hangman_art import stages
from Hangman_words import word_list
random_word = random.choice(word_list)

game_over = False
lives_left = 6

print(logo)

print("Pssstt... The random word chosen is '{}'".format(random_word))

display = []
for letter in range(len(random_word)):
    display += "_"
print(display)

while not game_over and lives_left > 0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed '{guess}'")
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display.pop(position)
            display.insert(position, letter)
    if guess not in random_word:
        print("Oh no!! '{}' is not in the word, You lose a life😩".format(guess))
        lives_left -= 1
        print(stages[lives_left])

    print(display)

    if "_" not in display:
        game_over = True
        print(f"{' '.join(display)}")
        print("You win !!!")


if lives_left == 0:
    print("Sorry you loose")
