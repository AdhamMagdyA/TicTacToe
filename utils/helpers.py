# print the board in console
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

# checks if a specific position is empty
def isPositionFree(board,position):
    return board[position] == ' '

# checks for draw
def isFull(board):
    for key in board:
        if isPositionFree(board,key):
            return False
    return True

# checks for a winner
def isWinner(board):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' ') :
        return True
    if (board[4] == board[5] and board[4] == board[6] and board[4] != ' ') :
        return True
    if (board[7] == board[8] and board[7] == board[9] and board[7] != ' ') :
        return True
    if (board[1] == board[4] and board[1] == board[7] and board[1] != ' ') :
        return True
    if (board[2] == board[5] and board[2] == board[8] and board[2] != ' ') :
        return True
    if (board[3] == board[6] and board[3] == board[9] and board[3] != ' ') :
        return True
    if (board[1] == board[5] and board[1] == board[9] and board[1] != ' ') :
        return True
    if (board[7] == board[5] and board[7] == board[3] and board[7] != ' ') :
        return True
    return False

def isWinnerMark(board,mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark) :
        return True
    if (board[4] == board[5] and board[4] == board[6] and board[4] == mark) :
        return True
    if (board[7] == board[8] and board[7] == board[9] and board[7] == mark) :
        return True
    if (board[1] == board[4] and board[1] == board[7] and board[1] == mark) :
        return True
    if (board[2] == board[5] and board[2] == board[8] and board[2] == mark) :
        return True
    if (board[3] == board[6] and board[3] == board[9] and board[3] == mark) :
        return True
    if (board[1] == board[5] and board[1] == board[9] and board[1] == mark) :
        return True
    if (board[7] == board[5] and board[7] == board[3] and board[7] == mark) :
        return True
    return False

from utils.minimax import minimax

# insert a symbol in a specific position
def insertLetter(board,letter,position):
    if isPositionFree(board,position):
        board[position] = letter
    else:
        newPosition = int(input("That position is already taken. \nPlease choose another position: "))
        insertLetter(board,letter,newPosition)

def player1Turn(board):
    position = int(input("Player o, choose a position: "))
    insertLetter(board,'o',position)

def player2Turn(board):
    position = int(input("Player x, choose a position: "))
    insertLetter(board,'x',position)

def computerTurn(board,depth):
    bestScore = -1000
    bestPosition = 0
    for key in board:
        if isPositionFree(board,key):
            board[key] = 'x'
            score = minimax(board,depth,'o')
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestPosition = key
    insertLetter(board,'x',bestPosition)
    return