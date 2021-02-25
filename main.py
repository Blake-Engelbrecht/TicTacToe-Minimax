"""
Project:            TicTacToe-Minimax
Contributors:       Blake Engelbrecht
Date:               2/26/2021
Description:        Unbeatable A.I. bot using a minimax algorithm python implementation
                    Player can choose to play against an easy or hard bot. The easy bot 
                    makes moves at random. The hard bot makes the best possible move.               
Board layout:     7|8|9
                  -----
                  4|5|6
                  -----
                  1|2|3
"""
import random 

def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("\n")

# ensures attempted move is valid 
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Cat's game! (that means a draw in Tic-Tac-Toe lingo) \n")
            exit()
        if checkForWin():
            if letter == botLetter:
                print("Bot wins! (of course because it is unbeatable...) \n")
                exit()
            else:
                print("Player wins! (wow you must be on easy mode, so impressive...) \n")
                exit()

        return


    else:
        print("Invalid move")
        position = int(input("Enter new move:  "))
        insertLetter(letter, position)
        return

# determines winner of game based on current board layout by checking horizontal, vertical and diagonal position
def checkForWin():
        # checks rows of board
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):     # bottom row
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):   # middle row
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):   #top row
        return True
        # checks columns of board
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):   # left column
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):   # middle column
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):   # right column
        return True
        # check diagonals of board
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):   # diagonal right-to-left
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):   # diagonal left-to-right
        return True
    else:
        return False

# 'simulated' board based on current move used by minimax algorithm to determine best possible move
def checkWhichMarkWon(mark):
        # checks rows of board
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):     # bottom row
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):   # middle row
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):   #top row
        return True
        # checks columns of board
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):   # left column
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):   # middle column
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):   # right column
        return True
        # check diagonals of board
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):   # diagonal right-to-left
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):   # diagonal left-to-right
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def playerMove():
    position = int(input("Enter move:  "))
    insertLetter(playerLetter, position)
    return

# easy mode bot to boost players confidence
def dumbBotMove():
    dBotPosition = ((random.randrange(8)+1))
    if spaceIsFree(dBotPosition):
        insertLetter(botLetter, dBotPosition)
        return
    else:
        dumbBotMove()

# unbeatable bot that will either win or tie
def botMove():
    bestScore = -999
    bestMove = 0

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = botLetter
            score = minimax(board, 0, False)    # uses minimax algorithm to find best move
            board[key] = ' '                    # resets move. Just want score of the move, not to actually make the move
            if (score > bestScore):             # updates best score to ensure bot is making the best possible move
                bestScore = score
                bestMove = key

    insertLetter(botLetter, bestMove)           # returns best move found by bot minimax algorithm
    return

# algorithm used to determine best possible move for bot. Gives each possible move a score, maximizing bot score and minimizing player score
def minimax(board, depth, isMaximizing,):
    if (checkWhichMarkWon(botLetter)):
        return 1
    elif (checkWhichMarkWon(playerLetter)):
        return -1
    elif (checkDraw()):
        return 0

# simulates moves for both player and bot based on current board layout. maximizes score for bot, minimizes score for player
    if (isMaximizing):
        bestScore = -999
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = botLetter
                score = minimax(board, depth + 1, False) # bot turn
                board[key] = ' ' # resets the board because we only want the score, not for the move to actually be made
                if (score > bestScore): # ensures bot has HIGHEST score
                    bestScore = score
        return bestScore

    else:
        bestScore = 999
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = playerLetter
                score = minimax(board, depth + 1, True) # player turn
                board[key] = ' '
                if (score < bestScore): # ensures player has the LOWEST score
                    bestScore = score
        return bestScore

print ('\n')
print('---------------------')
print('     Tic-Tac-Toe     ')
print('         vs.         ')
print('  The Unbeatable Bot ')
print('      (good luck)    ')
print('---------------------')
print('\n')
print('Board Layout:    7|8|9')
print('                 -----')
print('                 4|5|6')
print('                 -----')
print('                 1|2|3')

board = {7: ' ', 8: ' ', 9: ' ',
        4: ' ', 5: ' ', 6: ' ',
        1: ' ', 2: ' ', 3: ' '}

printBoard(board)
print('Difficulty Options:')
print('1. Easy')
print('2. Hard')
gameDifficulty = int(input('Select game difficulty (Enter 1 or 0): '))

playerLetter = input('Do you want to be X\'s or O\'s? X\'s always go first. (Enter "X" or "O"): ')
botLetter = 'X'

# very basic input validation because lazy
if playerLetter == 'X' or playerLetter == 'x':
    playerLetter = 'X'
    botLetter = 'O'
elif playerLetter == 'O' or playerLetter == 'o':
    playerLetter = 'O'
    botLetter == 'X'
else:
    print('\nInvalid input \n')
    exit()
# Determines difficulty and move order based on player selection, whoever is 'X' goes first
while not checkForWin():
    if playerLetter == 'X' and gameDifficulty == 1:
        playerMove()
        dumbBotMove()
    elif playerLetter == 'O' and gameDifficulty == 1:
        dumbBotMove()
        playerMove()
    elif playerLetter == 'X' and gameDifficulty == 2:
        playerMove()
        botMove()
    elif playerLetter == 'O' and gameDifficulty == 2:
        botMove()
        playerMove()
    else:
        print('\nFailed to follow simple instructions, game terminated. \n')
        exit()
    

