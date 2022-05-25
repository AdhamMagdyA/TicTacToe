from utils.helpers import *

board1 = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

print("Welcome to Tic-Tac-Toe!")
print("Player Human is 'o' and Computer is 'x' \n")


depth = 10

difficulty = input("Choose a difficulty level: \n1. Easy \n2. Hard \n")
if difficulty == '1':
    depth = 1
elif difficulty == '2':
    depth = 10
else:
    print("Invalid input. difficulty is set to Hard.")

print("\nEnter a position from 1 to 9 to place your mark according to the following board:")
print("1|2|3")
print("-+-+-")
print("4|5|6")
print("-+-+-")
print("7|8|9")
print("==================================================\n")

printBoard(board1)

while True:
    # player 1 turn
    player1Turn(board1)
    printBoard(board1)
    # check if game ends
    if isWinner(board1):
        print("Player o wins!")
        break
    elif isFull(board1):
        print("It's a draw!")
        break
    ####################
    # player 2 turn
    # player2Turn(board1)
    ####################
    print('Computer is thinking...')
    computerTurn(board1,depth)
    printBoard(board1)
    # check if game ends
    if isWinner(board1):
        print("Computer wins!")
        break
    elif isFull(board1):
        print("It's a draw!")
        break
    ####################
