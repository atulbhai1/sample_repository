import pygame as p
from Chess import ChessEngine
from tkinter.messagebox import showinfo
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
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    winner = None
    won = False
    while running and not won:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                continue
            elif e.type == p.MOUSEBUTTONDOWN:
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
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
            print(len(validMoves))
        whiteSurvives = False
        blackSurvives = False
        for row in gs.board:
            if 'wK' in row:
                whiteSurvives = True
            if 'bK' in row:
                blackSurvives = True
        if not blackSurvives or not whiteSurvives:
            if blackSurvives:
                winner = 'Black'
            else:
                winner = 'White'
            won = True
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
    p.quit()
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