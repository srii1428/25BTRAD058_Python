#Dice simulator using random module.
#* Develop a Python program that simulates rolling one or more dice using Python random
#module. Allow repeated rolls and display the outcomes.
# * Select suitable random functions, design the simulation logic, test repeated trials, and
#analyze the frequency of possible outcomes.
# * Relate the simulation to board games and probability experiments ;interpret the observed
#outcomes across multiple rolls.

import random
while True:
    roll = random.randint(1, 6)
    print("Dice Result:", roll)
    ch = input("Roll again? (yes/no): ")
    if ch != "yes":
        break