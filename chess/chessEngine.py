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
        
        
    def makeMove(self,move):
        # takes a move as parameter and executes it
        # wiil not work for castling, pawn promotion, en-passant
        self.board[move.startRow][move.startCol]='--'
        self.board[move.endRow][move.endCol]=move.pieceMoved
        self.moveLog.append(move)   # log the move so we can undo it later
        self.whiteToMove= not self.whiteToMove  # swap players
        
        
    def undoMove(self):
        if len(self.moveLog)!=0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol]=move.pieceMoved
            self.board[move.endRow][move.endCol]=move.pieceCaptured
            self.whiteToMove= not self.whiteToMove
    
    
    
class Move():
    
    ranksToRows = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
    rowsToRanks = {v:k for k,v in ranksToRows.items()}
    
    filesToCols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    colsToFiles = {v:k for k,v in filesToCols.items()}
    
    
    def __init__(self,startSquare,endSquare, board):
        self.startRow=startSquare[0]
        self.startCol=startSquare[1]
        self.endRow=endSquare[0]
        self.endCol=endSquare[1]
        self.pieceMoved=board[self.startRow][self.startCol]
        self.pieceCaptured=board[self.endRow][self.endCol]
        
        
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
        
    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]