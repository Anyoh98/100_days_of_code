# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
test_seed = int(input("Create your own seed number: "))
random.seed(test_seed)
random_side = random.randint(0, 1)
if (random_side == 0):
    print("Tail")
else:
    print("Head")
