from utils.helpers import *

def minimax(board,depth,player):
    if(depth == 0 or isWinnerMark(board,'x') or isWinnerMark(board,'o')):
        if isWinnerMark(board,'x'):
            return 1
        elif isWinnerMark(board,'o'):
            return -1
        else:
            return 0
    if isWinnerMark(board,'x'):
        return 1
    if isWinnerMark(board,'o'):
        return -1
    if isFull(board):
        return 0
    if player == 'x':
        best = -1000
        for key in board:
            if isPositionFree(board,key):
                board[key] = 'x'
                best = max(best,minimax(board,depth-1,'o'))
                board[key] = ' '
        return best
    else:
        best = 1000
        for key in board:
            if isPositionFree(board,key):
                board[key] = 'o'
                best = min(best,minimax(board,depth-1,'x'))
                board[key] = ' '
        return best
