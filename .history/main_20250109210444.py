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
      "to discover the hidden treasure, but none have prevailed.\n")
print("As a seasoned explorer, you took it upon yourself to try to be the first person to discover the hidden treasure.\n")

print("Your mission is to find the hidden treasure unharmed. Your choices matter.\n")

print('''
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⠿⢿⣿⣿⣿⣿⡿⠿⠟⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⢸⡇⢸⡇⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⠀⠀⠈⠛⢿⣿⣿⣿⣿⣶⣾⡇⢸⣷⣶⣿⣿⣿⣿⡿⠛⠁⠀⠀⣠⣾⣿
⣿⣿⣿⣷⣄⠀⠀⠀⠈⠻⢿⣿⣿⣿⡇⢸⣿⣿⣿⡿⠟⠁⠀⠀⠀⣠⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠙⠻⣿⣷⣾⣿⠟⠋⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣯⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿
''')

print("\nAs you go deeper into the jungle, you come across a crossroads.\n"
      "The left path is one of which many explorers have previously followed, "
      "while the right is an uncharted path.")

firstChoice = input("\nDo you want to go left or right?\n\n").lower()

if firstChoice == "left":
    # Prompt for user choosing "left" option
    print('''
           ."`".
       .-./ _=_ \.-.
      {  (,(oYo),) }}
      {{ |   "   |} }
      { { \(---)/  }}
      {{  }'-=-'{ } }
      { { }._:_.{  }}
      {{  } -:- { } }
      {_{ }`===`{  _}
     ((((\)     (/))))
    ''')

    print("\nWise choice. As you continue on your journey, you stumble upon a rabid baboon staring you\n"
          "down in the middle of the trail. Baboons are known to be rife with violence.\n"
          "You could either stand your ground and fight it or run away from it.")
    
    secondChoice = input("\nFight or flight?\n\n").lower()

    if secondChoice == "fight":
        # Prompt for choosing "fight" option
        print('''
|                         |    |                        |
|                    \__r'|    |             .   ~   .  |
|                   o'   \|    | -oof-                  |
|                      '  |    |      o_  '             |
|         o               |    |     (       ro         |
|        '=\    _  -  '   |    |      \  * -{ `         |
|        r \              |    |             \          |
'"""""""""""""""""""""""""'    '""""""""""""""""""""""""'               
        ''')

        print("You charge towards the baboon and it charges towards you, until you meet in the middle and start wrestling.\n"
              "It\'s a tough fight, but you finally RKO that baboon and continue on your way until you\'ve finally reached\n"
              "the heart of the jungle where a mysterious temple stands.\n")
        
        print('''
                     |
                   .' `.
                : (     ) :
     .      |  ( )`._ _.'( )  |      .
     O  .   |`-  -|  .  |-  -'|   .  O
     H  o   |A /\ | ( ) | /\ A|   o  H
     H  I   |  -' | | | | `-  |   I  H
    .H__T___|_|___|_|_|_|___|_|___T__H.
    |_________________________________|
                 /       \  
                /         \ 
               /           \ ''')

        print("\nIts ancient stone walls are covered in thick vines and strange glowing symbols that pulse with an otherworldly blue light.\n"
              "The massive doorway seems to beckon you forward, but as you approach, you notice something odd - there's no door, just a\n" 
              "shimmering barrier of energy that ripples like water. Through the barrier, you can only make out what appears to be\n" 
              "a golden idol sitting atop a pedestal. Would you like to try to walk through the barrier, look for another way in,\n"
              "or throw a rock at the barrier to test it?")
        
        thirdChoice = input("\nWalk, look, or throw?\n\n").lower()

        if thirdChoice == "walk":
            print('''          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁

⠀⠀⠀⠀⠀YOUR TIME HAS COME 🈵⠀       
            ''')

            print("\nYou bravely step into the shimmering barrier, but instantly feel your body being "
                  "ripped apart by the ancient magic. Game over.\n")
            exit()
        elif thirdChoice == "look":
            print("\nAs you circle the temple looking for another entrance, you accidentally trigger "
                  "a trap door and fall into a pit of spikes. Game over.\n")
            exit()
        elif thirdChoice == "throw":
            print("\nThe rock passes through the barrier and topple over the golden idol. The barrier dissipates!\n"
                  "You walk into the temple to find mounds of gold and jewels that flood the room.\n"
                  "You've completed your quest! YOU WIN!\n")
            exit()
        else:
            print("\nAs you gaze at the temple confused, a strange being comes up behind you and snaps your neck. Game over.\n")

    elif secondChoice == "flight":
        print("\nAs you take off running, the baboon charges after you. Right when you think " 
              "you\'ve gained advantage,\nyou trip on a tree root and the baboon tackles you and bites your face off. "
              "Game over.\n")
        exit()

    else:
        print("\nYou freeze up in front of the baboon and it mauls you before you could think to do anything reasonable. Game over.\n")
        exit()

elif firstChoice == "right":
    print("\nAs you continue your trek into the jungle, you fall into a sink hole.\n"
          "Dumbass. Game over.\n")
    exit()

else:
    print("\nWrong way. You fall off a cliff and die a stupid death. Game over.\n")
    exit()
