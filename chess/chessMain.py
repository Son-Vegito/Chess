'''
main driver file
responsible for handling user input and displaying the current gamestate object
'''

import pygame
import chessEngine
pygame.init()

WIDTH = 400
HEIGHT = 400
DIMENSIONS = 8
SQUARE_SIZE = HEIGHT//DIMENSIONS
FPS = 30
IMAGES={}

# initializing a global dictionary of images.
# this will be called exactly once in the main loop
def loadImages():
    pieces=['bR','bN','bB','bQ','bK','bP','wR','wN','wB','wQ','wK','wP']
    for piece in pieces:
        IMAGES[piece]=pygame.transform.scale(pygame.image.load("Chess/chess/images/"+piece+".png"),(SQUARE_SIZE,SQUARE_SIZE))
        
    # we can access an image by using 'IMAGE[piece]'
    

# main driver
# handle user input and update graphics
def main(): 
    screen= pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('White'))
    gs=chessEngine.GameState()
    
    validMoves=gs.getValidMoves()
    
    loadImages()
    running = True
    squareSelected=()   #keeps track of the last click of the user
    playerClicks=[]     #keeps track of player's click [list(tuples)]
    
    while(running):
        
        moveMade = False    # flag variable to check if a move is made
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            # mouse handler
            elif event.type==pygame.MOUSEBUTTONDOWN:
                location=pygame.mouse.get_pos() 
                col=location[0]//SQUARE_SIZE
                row=location[1]//SQUARE_SIZE
                
                if squareSelected==(row,col):
                    squareSelected=()
                    playerClicks=[]
                else:
                    squareSelected=(row,col)
                    playerClicks.append(squareSelected)
                    
                if len(playerClicks)==2:
                    move=chessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    if move in validMoves:
                        print(move.getChessNotation())
                        gs.makeMove(move)
                        moveMade=True
                    # reset
                    squareSelected=()
                    playerClicks=[]
                
            # key handler
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gs.undoMove()
                    moveMade=True
        
        if moveMade:
            validMoves=gs.getValidMoves()
            moveMade=False
        
        drawGameState(screen,gs)
        clock.tick(FPS)
        pygame.display.flip()
        
        
# responsible for all graphics within a current game state
def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)
        
        
# draw the square on the board
def drawBoard(screen):
    colours = [pygame.Color("white"),pygame.Color("gray")]
    
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            colour=colours[(r+c)%2]
            pygame.draw.rect(screen,colour,(c*SQUARE_SIZE,r*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                
        
        
# draw the pieces on the board using the GameState.board
def drawPieces(screen,board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece !='--':
                screen.blit(IMAGES[piece],(c*SQUARE_SIZE,r*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
        
        
if __name__=="__main__":
    main()