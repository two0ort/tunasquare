from stockfish import Stockfish

# Change Stockfish settings
sf = Stockfish(path="/home/two0ort/Applications/stockfish/stockfish-ubuntu-x86-64-avx2")
sf.set_elo_rating(1500)

# Show board
print(sf.get_board_visual())

# Game loop
while True:
    # Ask for move
    print("Enter move: ")
    myMove = input()
    # Make move on virtual board
    sf.make_moves_from_current_position([myMove])
    # Let Stockfish move
    fishMove = sf.get_best_move()
    print("Stockfish plays ", fishMove)
    # Make move again
    sf.make_moves_from_current_position([fishMove])
    #Show the board
    print(sf.get_board_visual())