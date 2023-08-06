import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇


Your_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))
if (Your_choice == 0):
    print(rock)
elif (Your_choice == 1):
    print(paper)
elif (Your_choice == 2):
    print(scissors)
else:
    print("Your choice is invalid, try again.")


Computer_choice = random.randint(0, 2)
if (Computer_choice == 0):
    print("Computer chose: ")
    print(rock)
elif (Computer_choice == 1):
    print("Computer chose: ")
    print(paper)
elif (Computer_choice == 2):
    print("Computer chose: ")
    print(scissors)

# rules of the game

if (Your_choice == Computer_choice):
    print("It is a tie!!")
elif (Your_choice == 0):
    if (Computer_choice == 1):
        print("You lose!😩")
    elif (Computer_choice == 2):
        print("You win!")
elif (Your_choice == 1):
    if (Computer_choice == 0):
        print("You win!🥳")
    elif (Computer_choice == 2):
        print("You lose!😩")
elif (Your_choice == 2):
    if (Computer_choice == 0):
        print("You lose!😩")
    elif (Computer_choice == 1):
        print("You win!🥳")
