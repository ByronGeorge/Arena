import enemy
import textwrap
import armor
import classes
import weapons

e1 = enemy.Enemy(10, 10, 2, 1, 0, 4, 1, 1, 1, 1)

game = True # Boolean to keep game loop alive. Will set this to false when we want the game to end. - BG

menuText = textwrap.dedent("""\

    Please choose an option:

    1. New Game
    2. Load Game
    3. Options
    4. Quit Game
    """)

choiceCursor = textwrap.dedent("""       
 >>-->> """)



while(game):

    print(menuText)
    menuChoice = int(input(choiceCursor))

    if menuChoice == 1:
        # New Game
        print("New Game") 
    elif menuChoice == 2:
        # Load Game
        print("Load Game")
    elif menuChoice == 3:
        # Options
        print("Options")
    elif menuChoice == 4:
        # Quit Game
        print("Quitting Game")
        game = False
    


#print (menuText)
print(e1.health)
print(e1.mana)
