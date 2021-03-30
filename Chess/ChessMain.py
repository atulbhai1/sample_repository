import pygame as p
from Chess import ChessEngine
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'wp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (SQ_SIZE, SQ_SIZE))
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                row = location[1] // SQ_SIZE
                col = location[0] // SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], board=gs.board)
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
def drawGameState(scr, g):
    drawBoard(scr)
    drawPieces(scr, g)
def drawBoard(scr):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(scr, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
def drawPieces(scr, g):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = g.board[r][c]
            if piece != '--':
                scr.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
if __name__ == '__main__':
    main()
    #