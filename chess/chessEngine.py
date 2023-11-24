'''
responsible for storing all the information about the current state of the game
respondible for determining the valid moves at the current state
will also keep a move log
'''

class GameState():
    def __init__(self):
        
        # board is 8X8 2d list, each element of the list has 2 characters
        # the first character represents the colour of the pieces, 'b' for 'black' and 'w' for 'white'
        # the second character represents the type of the piece, 'K', 'Q', 'B', 'N', 'R' or 'P'
        # '--' represents empty space where no piece is present 
        self.board=[
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wP','wP','wP','wP','wP','wP','wP','wP'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']
        ]
        self.whiteToMove=True
        self.moveLog=[]