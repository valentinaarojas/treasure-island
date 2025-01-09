print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

firstChoice = input("Upon exploring the jungle of the island, you've reached a crossroad. Do you want to go left or right?\n").lower()

if(firstChoice == "right"):
    print("You fell into a hole. Game over.")
    exit()

secondChoice = input("Swim or wait?").lower()

if(secondChoice == "swim"):
    print("Attacked by a piranha. Game over.")
    exit()

thirdChoice = input("Which door? Red, blue, or yellow?").lower()

if(thirdChoice == "red"):
    print("Burned by fire. Game over.")
elif(thirdChoice == "blue"):
    print("Eaten by beasts. Game over.")
elif(thirdChoice == "yellow"):
    print("You win!")
