class GameState:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
             ['--', '--', '--', '--', '--', '--', '--', '--'],
             ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
             ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.moveFunctions = {'p':self.getPawnMoves, 'R':self.getRookMoves, 'N':self.getKnightMoves, 'B':self.getBishopMoves, 'Q' :self.getQueenMoves, 'K':self.getKingMoves}
        self.whiteToMove = True
        self.moveLog = []
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                 turn = self.board[r][c][0]
                 if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                     piece = self.board[r][c][1]
                     self.moveFunctions[piece](r=r, c=c, moves=moves)
        return moves
    def getPawnMoves(self, r, c, moves):
         if self.whiteToMove:
            if self.board[r-1][c] == '--':
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == '--':
                    moves.append(Move((r, c), (r-2, c), self.board))
            if c - 1 >= 0:
                if self.board[r-1][c-1] != '--':
                    if self.board[r-1][c-1][0] != 'w':
                        moves.append(Move((r, c), (r-1, c-1), self.board))
            if c + 1 < 8:
                if self.board[r-1][c+1] != '--':
                    if self.board[r - 1][c + 1][0] != 'w':
                        moves.append(Move((r, c), (r-1, c+1), self.board))
         else:
            if self.board[r+1][c] == '--':
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == '--':
                    moves.append(Move((r, c), (r+2, c), self.board))
            if c - 1 >= 0:
                if self.board[r+1][c-1] != '--':
                    if self.board[r+1][c-1][0] != 'b':
                        moves.append(Move((r, c), (r+1, c-1), self.board))
            if c + 1 < 8:
                if self.board[r+1][c+1] != '--':
                    if self.board[r + 1][c + 1][0] != 'b':
                        moves.append(Move((r, c), (r+1, c+1), self.board))
    def getRookMoves(self, r, c, moves):
        for exR in  range(r - 1, -1, -1):
            if self.board[exR][c] == '--':
                moves.append(Move((r, c), (exR, c), self.board))
            else:
                if self.board[exR][c][0] != self.board[r][c][0]:
                    moves.append(Move((r, c), (exR, c), self.board))
                break
        for exR in range(r + 1, 8):
            if self.board[exR][c] == '--':
                moves.append(Move((r, c), (exR, c), self.board))
            else:
                if self.board[exR][c][0] != self.board[r][c][0]:
                    moves.append(Move((r, c), (exR, c), self.board))
                break
        for exC in range(c - 1, -1, -1):
            if self.board[r][exC] == '--':
                moves.append(Move((r, c), (r, exC), self.board))
            else:
                if self.board[r][exC][0] != self.board[r][c][0]:
                    moves.append(Move((r, c), (r, exC), self.board))
                break
        for exC in range(c + 1, 8):
            if self.board[r][exC] == '--':
                moves.append(Move((r, c), (r, exC), self.board))
            else:
                 if self.board[r][exC][0] != self.board[r][c][0]:
                     moves.append(Move((r, c), (r, exC), self.board))
                 break
    def getKnightMoves(self, r, c, moves):
         if r - 2 > -1 and c - 1 > -1:
             move = Move((r, c), (r - 2, c - 1), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r - 2 > -1 and c + 1 < 8:
             move = Move((r, c), (r - 2, c + 1), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r - 1 > -1 and c - 2 > -1:
             move = Move((r, c), (r - 1, c - 2), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r - 1 > -1 and c + 2 < 8:
             move = Move((r, c), (r - 1, c + 2), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r + 2 < 8 and c - 1 > -1:
             move = Move((r, c), (r + 2, c - 1), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r + 2 < 8 and c + 1 < 8:
             move = Move((r, c), (r + 2, c + 1), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r + 1 < 8 and c - 2 > -1:
             move = Move((r, c), (r + 1, c - 2), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
         if r + 1 < 8 and c + 2 < 8:
             move = Move((r, c), (r + 1, c + 2), self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0]:
                 moves.append(move)
    def getBishopMoves(self, r, c, moves):
         for ex in range(r - 1, -1, -1):
             if c - (r - ex) > -1:
                 if self.board[ex][c - (r - ex)] == '--':
                     moves.append(Move((r, c), (ex, c - (r - ex)), self.board))
                 else:
                     if self.board[ex][c - (r - ex)][0] != self.board[r][c][0]:
                         moves.append(Move((r, c), (ex, c - (r - ex)), self.board))
                     break
         for ex in range(r + 1, 8):
             if c - (ex - r) > -1:
                 if self.board[ex][c - (ex - r)] == '--':
                     moves.append(Move((r, c), (ex, c - (ex - r)), self.board))
                 else:
                     if self.board[ex][c - (ex - r)][0] != self.board[r][c][0]:
                         moves.append(Move((r, c), (ex, c - (ex - r)), self.board))
                     break
         for ex in range(r - 1, -1, -1):
             if c + (r - ex) < 8:
                 if self.board[ex][c + (r - ex)] == '--':
                     moves.append(Move((r, c), (ex, c + (r - ex)), self.board))
                 else:
                     if self.board[ex][c + (r - ex)][0] != self.board[r][c][0]:
                         moves.append(Move((r, c), (ex, c + (r + ex)), self.board))
                     break
         for ex in range(r + 1, 8):
             if c + (ex - r) < 8:
                 if self.board[ex][c + (ex - r)] == '--':
                     moves.append(Move((r, c), (ex, c + (ex - r)), self.board))
                 else:
                     if self.board[ex][c + (ex - r)][0] != self.board[r][c][0]:
                         moves.append(Move((r, c), (ex, c - (ex + r)), self.board))
                     break
    def getQueenMoves(self, r, c, moves):
         self.getRookMoves(r, c, moves)
         self.getBishopMoves(r, c, moves)
    def getKingMoves(self, r, c, moves):
         pMoves = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                   (r, c - 1), (r, c + 1),
                   (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
         if r == 0:
             pMoves.remove((r - 1, c - 1))
             pMoves.remove((r - 1, c))
             pMoves.remove((r - 1, c + 1))
         elif r == 7:
             pMoves.remove((r + 1, c - 1))
             pMoves.remove((r + 1, c))
             pMoves.remove((r + 1, c + 1))
         if c == 0:
             if (r - 1, c - 1) in pMoves:
                 pMoves.remove((r - 1, c - 1))
             if (r + 1, c - 1) in pMoves:
                 pMoves.remove((r + 1, c - 1))
             pMoves.remove((r, c - 1))
         elif c == 7:
             if (r - 1, c + 1) in pMoves:
                 pMoves.remove((r - 1, c + 1))
             if (r + 1, c + 1) in pMoves:
                 pMoves.remove((r + 1, c + 1))
             pMoves.remove((r, c + 1))
         for moveTemplate in pMoves:
             move = Move((r, c), moveTemplate, self.board)
             if move.pieceMoved[0] != move.pieceCaptured[0] and move.pieceCaptured[1] != 'K':
                 moves.append(move)
class Move:
    ranksToRows = {'1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    colsToFiles = {v :k for k, v in filesToCols.items()}
    def __init__(self, startSQ, endSQ, board):
        self.startRow = startSQ[0]
        self.startCol = startSQ[1]
        self.endRow = endSQ[0]
        self.endCol = endSQ[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        print(self.moveID)
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False