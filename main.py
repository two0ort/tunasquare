# Config
# Path to your Stockfish executable
pathToStockfish = ("/home/two0ort/Applications/stockfish/stockfish-ubuntu-x86-64-avx2")

from stockfish import Stockfish

global sfELo

# Asks user to set the Elo rating of the Fish
def setElo():
    global eloMin, eloMax, sfElo
    eloMin = 1320
    eloMax = 3190
    sfElo = 0
    while sfElo < eloMin or sfElo > eloMax:
        sfElo = int(input("Set Stockfish's Elo: "))
        if sfElo < eloMin:
            print("The minimum Elo is 1320.")
        elif sfElo > eloMax:
            print("The maximum Elo is 3190.")
        else:
            pass
# Game Loop, run constantly after settings
def gameLoop():
    # Ask for move
    print("Enter move: ")
    myMove = input()
    # Make move on virtual board
    try:
        sf.make_moves_from_current_position([myMove])
        # Let Stockfish move
        fishMove = sf.get_best_move()
        print("Stockfish plays ", fishMove)
        # Make move again
        sf.make_moves_from_current_position([fishMove])
        #Show the board
        print(sf.get_board_visual())
    except ValueError:
        # Handle the exception here
        print("That move isn't legal, try again!")

sf = Stockfish(path=pathToStockfish)
setElo()
sf.set_elo_rating(sfElo)

print(sf.get_board_visual())
while True:
    gameLoop()