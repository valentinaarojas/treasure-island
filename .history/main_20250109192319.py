print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print("Welcome to Treasure Island.\n")

print("Since the dawn of the Age of Exploration, explorers from around the world have set out to seas\n"
      "in an attempt to discover the hidden treasure that is said to be located in the heart of the jungle of Treasure Island.\n") 
print("Christopher Columbus, Ferdinand Magellan, and even Marco Polo have all attempted\n" 
      "to discover the treasure, but none have prevailed.\n")
print("As a seasoned explorer, you took it upon yourself to try to be the first person to discover the hidden treasure.\n")

print("Your mission is to find the hidden treasure unharmed. Your choices matter.\n\n\n")

# Put ASCII art here

firstChoice = input("As you go deeper into the jungle, you come across a crossroads.\n"
                    "The left path is one of which many explorers have previously followed, "
                    "while the right is an uncharted path.\n" 
                    "\nDo you want to go left or right?\n").lower()

if firstChoice == "left":
    # Prompt for user choosing "left" option
    secondChoice = input("\nSwim or wait?\n").lower()
    if secondChoice == "wait":
        # Prompt for choosing "wait" option
        thirdChoice = input("\nWhich door? Red, blue, or yellow?\n").lower()

        if thirdChoice == "red":
            print("\nBurned by fire. Game over.")
        elif thirdChoice == "blue":
            print("\nEaten by beasts. Game over.")
        elif thirdChoice == "yellow":
            print("\nYou win!")

    elif secondChoice == "swim":
        print("\nAttacked by a piranha. Game over.")
        exit()

elif firstChoice == "right":
    print("As you continue your trek into the jungle, you fall into a sink hole. Game over.")
    exit()

else:
    print("Game over.")
