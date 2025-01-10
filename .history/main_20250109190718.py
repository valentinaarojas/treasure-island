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
      "in an attempt to discover the hidden treasure that is said to be located in the heart of the jungle\n"
      "of Treasure Island. Christopher Columbus, Ferdinand Magellan, and even Marco Polo have all attempted" 
      "to discover the treasure, but none have prevailed. As a seasoned explorer, you took it upon yourself\n"
      "to ")

print("Your mission is to find the hidden treasure unharmed. Your choices matter\n")

firstChoice = input("Upon exploring the jungle of the island, you've reached a crossroads. " 
                    "Do you want to go left or right?\n").lower()

if firstChoice == "left":
    # Prompt for user choosing "left" option
    secondChoice = input("Swim or wait?").lower()
    if secondChoice == "wait":
        # Prompt for choosing "wait" option
        thirdChoice = input("Which door? Red, blue, or yellow?").lower()

        if thirdChoice == "red":
            print("Burned by fire. Game over.")
        elif thirdChoice == "blue":
            print("Eaten by beasts. Game over.")
        elif thirdChoice == "yellow":
            print("You win!")

    elif secondChoice == "swim":
        print("Attacked by a piranha. Game over.")
        exit()

elif firstChoice == "right":
    print("You fell into a hole. Game over.")
    exit()

else:
    print("Game over.")
