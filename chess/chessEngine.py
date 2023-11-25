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
    
    
    # all moves considering checks
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    # all moves without considering checks
    def getAllPossibleMoves(self):
        moves=[]
        
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn =='w' and self.whiteToMove) or (turn=='b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece=='P':
                        self.getPawnMoves(r,c,moves)
                    elif piece == 'R':
                        self.getRookMoves(r,c,moves)
                    elif piece == 'B':
                        self.getBishopMoves(r,c,moves)
                    elif piece == 'Q':
                        self.getQueenMoves(r,c,moves)
        return moves
    
    def getPawnMoves(self,r,c,moves):
        if self.whiteToMove:    # white pawn move
            if self.board[r-1][c]=='--':    # 1 square move
                moves.append(Move((r,c),(r-1,c),self.board))
                if r==6 and self.board[r-2][c]=='--':   # 2 square move
                    moves.append(Move((r,c),(r-2,c),self.board))
            # capture
            if c>0 and self.board[r-1][c-1][0]=='b':
                moves.append(Move((r,c),(r-1,c-1),self.board))
            if c+1<len(self.board) and self.board[r-1][c+1][0]=='b':
                moves.append(Move((r,c),(r-1,c+1),self.board))
                
                
        else:   # black pawn move
            if self.board[r+1][c]=='--':    # 1 square move
                moves.append(Move((r,c),(r+1,c),self.board))
                if r==1 and self.board[r+2][c]=='--':   # 2 square move
                    moves.append(Move((r,c),(r+2,c),self.board))
            # capture
            if c>0 and self.board[r+1][c-1][0]=='w':
                moves.append(Move((r,c),(r+1,c-1),self.board))
            if c+1<len(self.board) and self.board[r+1][c+1][0]=='w':
                moves.append(Move((r,c),(r+1,c+1),self.board))
                    
                    
    def getRookMoves(self,r,c,moves):
        directions=((-1,0),(1,0),(0,-1),(0,1))  # up, down, left, right
        enemyColour='b'
        if self.whiteToMove:
            enemyColour='b'
        else:
            enemyColour='w'
            
        for d in directions:
            for i in range(1,8):
                newRow=r+d[0]*i
                newCol=c+d[1]*i
                
                if 0<=newRow<8 and 0<=newCol<8: # on board
                    endPiece=self.board[newRow][newCol]
                    if endPiece=='--':   # empty 
                        moves.append(Move((r,c),(newRow,newCol),self.board))
                    elif endPiece[0]==enemyColour: # emeny piece capture
                        moves.append(Move((r,c),(newRow,newCol),self.board))
                        break
                    else:   # friendly piece
                        break
                else:   # off board
                    break
    
    
    def getBishopMoves(self,r,c,moves):
        directions=((-1,-1),(1,1),(-1,1),(1,-1))  # up, down, left, right
        enemyColour='b'
        if self.whiteToMove:
            enemyColour='b'
        else:
            enemyColour='w'
            
        for d in directions:
            for i in range(1,8):
                newRow=r+d[0]*i
                newCol=c+d[1]*i
                
                if 0<=newRow<8 and 0<=newCol<8: # on board
                    endPiece=self.board[newRow][newCol]
                    if endPiece=='--':   # empty 
                        moves.append(Move((r,c),(newRow,newCol),self.board))
                    elif endPiece[0]==enemyColour: # emeny piece capture
                        moves.append(Move((r,c),(newRow,newCol),self.board))
                        break
                    else:   # friendly piece
                        break
                else:   # off board
                    break    
    
    
    def getQueenMoves(self,r,c,moves):
        self.getRookMoves(r,c,moves)
        self.getBishopMoves(r,c,moves)
    
    
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
        self.moveID=self.startRow*1000+self.startCol*100+self.endRow*10+self.endCol
        
    # overriding the equals method
    def __eq__(self,other):
        if isinstance(other, Move):
            return self.moveID==other.moveID
        return False
        
        
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
        
    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]