import pygame as p
from Chess import ChessEngine
from tkinter.messagebox import showinfo
HEIGHT = 512
WIDTH = 712
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
p.init()
def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'wp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (SQ_SIZE, SQ_SIZE))
def main():
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
                if len(playerClicks) == 1 and gs.board[sqSelected[0]][sqSelected[1]] == '--':
                    playerClicks = []
                    sqSelected = ()
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
            continue
        drawGameState(screen, gs, sqSelected)
        clock.tick(MAX_FPS)
        p.display.flip()
    p.quit()
oldPiece = None
def drawGameState(scr, g, sq):
    drawBoard(scr)
    drawPieces(scr, g)
    if len(sq) == 2:
        piece = g.board[sq[0]][sq[1]]
    else:
        piece = 'No Piece Selected'
    drawSelectedPiece(piece, scr)
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
font = p.font.Font('freesansbold.ttf', 20)
def drawSelectedPiece(pc, scr):
    global oldPiece
    scr.blit(font.render('You have selected:', True, (0, 0, 0)), (512, 100))
    if pc != '--' and pc != 'No Piece Selected':
        scr.blit(IMAGES[pc], (600, 200))
        if oldPiece is not None:
            scr.blit(oldPiece, (1000, 1000))
        oldPiece = IMAGES[pc]
if __name__ == '__main__':
    main()
    #