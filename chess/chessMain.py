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
    loadImages()
    running = True
    
    while(running):
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

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