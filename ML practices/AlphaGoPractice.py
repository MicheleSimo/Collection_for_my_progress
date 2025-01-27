import numpy as np
import board

def getInitBoard():
    return np.zeros((6,7))

def place_piece(bordo, player, action):
    row_index = sum(bordo[:,action] == 0) - 1
    bordo[row_index,action] = player
    return board

    

bordo = getInitBoard()
place_piece(bordo,player=1,action=3)

print(bordo)
board.render(bordo)