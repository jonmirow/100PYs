# Serial Killer Name Generator

# Goals: 

# 1 Ask for three names:
    # a) First name of their favourite grandparent
    # b) name of their pet
    # c) surname of their favourite teacher

# 2 Suggest the names in the order asked
    # Not needed with itertools.permutations
    #Loop through generator. 

# Ask if user likes the name, if not offer a random order of the names. 

# when the user is happy, or they've heard all possiblitities (6), exit. 
    # this should be a generator
    #Google suggeests itertools.permutaions
from itertools import permutations
count = 0
name = ""
print("Welcome to the Serial Killer Name Generator.\nYou will be asked a series of questions, answer as honestly as you can.")
input(("Press Return to continue..."))
first = input("\n\n\nWhat was the first name of your favourite grandparent?\n")
second = input("\n\n\nOk, what's your pet's name?\n")
third = input("\n\n\nFinally, what was the surname of your favourite teacher?")

killers = permutations((first, second, third), 3)

for killer in killers:
    name = " ".join(killer).title()
    count += 1
    if count > 1:
        print("\n\n\nNot happy with that, huh?, fine ...")
    print(f"Your Serial Killer name is {name}!")
    answer = input("\n\n\nHappy with that? Enter 'no', 'nope' or 'nada' if not: ")
    if not answer or answer[0] not in "Nn":
        break
if count == 6:
    print("\n\n\nWell, that's all the options! \n ... \n soooo \n ...")

print(f"Great, your seriall killer name is {name} !")
