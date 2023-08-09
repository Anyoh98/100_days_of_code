import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)

print("Pssstt... The random word chosen is {""}".format(random_word))

display = []
i = 0
for letter in random_word:
    display.insert(i, "_")
    i += 1
print(display)

game_over = False
lives_left = 6

while not game_over and lives_left > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display.pop(position)
            display.insert(position, letter)
    if guess not in random_word:
        print("Please ill be hung, character wasnt correct😭😭😭!")
        lives_left -= 1
    print(display)

    if "_" not in display:
        game_over = True
        print(f"{' '.join(display)}")
        print("You win !!!")


if lives_left == 0:
    print("Sorry you loose")
