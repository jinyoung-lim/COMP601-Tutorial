""" File: PebbleSolitaire.py
Author: JJ Lim
Date: Oct 2017 - Nov 2017

A class dedicated to solve "Pebble Solitaire" problem from Open Kattis (https://open.kattis.com/problems/pebblesolitaire).
"""

# WORK WITH DFS
#     - cavity -> look at possible moves -> move! and make copies!
#     - compare copies in the end!

def main():
    boards = readPebbleFile("pebblesolitaire.in")
    numGames = boards.pop(0)
    for board in boards:
        print(board)
        print(getMinPebbles(board))
        print()


def dfsPebbles(board):
    '''Use depth-first search to move the cavities
    :param board: list of integers containing information about the pebble solitaire board. Empty pebbles are noted
     with 0, cavities are noted with 1.
    :return: a copy of the board after moving a cavity, return None if cannot move anymore
    '''
    boardCopy = board


    # preds = {}
    # visited = []
    # frontierStack = []
    #
    # preds[startInd] = -1
    # visited.append(startInd)
    # frontierStack.append(startInd)


    cavityInd = []
    for i in range(0, len(board)-1):
        if board[i] == 1:
            cavityInd.append(i)

    visited = []

    while(cavityInd):
        currInd = cavityInd.pop()
        visited.append(currInd)
        if (currInd < len(boardCopy)-3 and boardCopy[currInd + 1] == 1 and boardCopy[currInd + 2] == 0):
            # found the path to move right
            boardCopy[currInd] = 0
            boardCopy[currInd + 1] = 0
            boardCopy[currInd + 2] = 1
            # update the cavityInd list
            if (currInd + 1 in cavityInd):
                cavityInd.remove(currInd + 1)
            cavityInd.append(currInd + 2)

        if (currInd > 2 and boardCopy[currInd - 1] == 1 and boardCopy[currInd - 2] == 0):
            # found the path to move right
            boardCopy[currInd] = 0
            boardCopy[currInd - 1] = 0
            boardCopy[currInd - 2] = 1

            # update the cavityInd list
            if (currInd - 1 in cavityInd):
                cavityInd.remove(currInd - 1)
            cavityInd.append(currInd - 2)
        # else:
        #     neighs = [boardCopy[currInd - 1], boardCopy[currInd + 1]]
        #     for neigh in neighs:
        #         if (neigh not in visited):
        #             visited.append(neigh)
        #             # preds[neigh] = currInd
        #             # frontierStack.append(neigh)

    return boardCopy

def getMinPebblesAll(num, boards):
    pass

def getMinPebbles(board):
    boardCopy = board
    minCavities = boardCopy.count(1)
    # while (dfsPebbles(boardCopy)):
    #     boardCopy = dfsPebbles(boardCopy)
    #     print(boardCopy)
    #     numCavities = boardCopy.count(1)
    #     if (numCavities < minCavities):
    #         minCavities = numCavities
    return dfsPebbles(board).count(1)
    # numMoves = 12
    # for cavity in board:
    #     print(cavity, end=" ")
    # print()
    # while(numMoves >= 0):
    #     for cavity in board:
    #         print(cavity)
    #         checkLeft = checkEligibleMoveLeft(board, cavity)
    #         checkRight = checkEligibleMoveRight(board, cavity)
    #         print(checkRight)
    #         if checkLeft == checkRight:
    #             if checkRight >= 0:
    #                 moveLeft(board, cavity)
    #                 numMoves -= 1
    #             else:
    #                 numMoves -= 1
    #
    #         elif checkLeft > checkRight:
    #             moveLeft(board, cavity)
    #             numMoves -= 1
    #         else:
    #             moveRight(board, cavity)
    #             numMoves -= 1
    # for cavity in board:
    #     print(cavity, end=" ")
    # print()
    # return board.count(1)

def moveLeft(board, cavityPos):
    board[cavityPos] = 0
    board[cavityPos-1] = 0
    board[cavityPos-2] = 1

def moveRight(board, cavityPos):
    board[cavityPos] = 0
    board[cavityPos+1] = 0
    board[cavityPos+2] = 1

def checkEligibleMoveLeft(board, cavityPos):
    """Check if a given cavity can move to left, and if so, if it can move the next turn (a winning move)
    :param board: an integer array of length 12 containing pebble solitaire board information (empty cavities are noted
    with 0 and cavities with 1)
    :param cavityPos: position of the cavity on the board
    :return: a negative number(-1) if left move is not eligible; 0 if eligible but not a winning move; a positive
    number(1) if a winning left move
    """
    if cavityPos <= 1: #check for boundary
        return -1

    if board[cavityPos-1] == 1 and board[cavityPos-2] == 0:
        return 1 if (cavityPos >= 3 and board[cavityPos-3] == 1) else 0 #check for winning move
        # if cavityPos <= len(board) - 4 and board[cavityPos+3] == 1: #check for winning move
        #     return 2
        # else:
        #     return 1

    print("left")
    return -1


def checkEligibleMoveRight(board, cavityPos):
    """Check if a given cavity can move to right, and if so, if it can move the next turn (a winning move)
    :param board: an integer array of length 12 containing pebble solitaire board information (empty cavities are noted
    with 0 and cavities with 1)
    :param cavityPos: position of the cavity on the board
    :return: a negative number(-1) if right move is not eligible; 0 if eligible but not a winning move; a positive
    number(1) if a winning right move
    """
    if cavityPos >= len(board) - 2:  # check for boundary
        return -1

    if board[cavityPos + 1] == 1 and board[cavityPos + 2] == 0:
        return 1 if ((cavityPos <= len(board) - 4) and (board[cavityPos + 3] == 1)) else 0 #check for winning move
        # if cavityPos <= len(board) - 4 and board[cavityPos+3] == 1: #check for winning move
        #     return 2
        # else:
        #     return 1
    # print("right")
    return -1

def readPebbleFile(file):
    """Reads in the file with game information.
    :param file: begins with a positive integer n≤10 on a line of its own. Thereafter n different games
    follow. Each game consists of one line of input with exactly twelve characters, describing the twelve cavities of
    the board in order. Each character is either ‘-’ or ‘o’. A ‘-’ character denotes an empty cavity, whereas an ‘o’
    character denotes a cavity with a pebble in it. There is at least one pebble in all games
    :return: An array containing number of game information at start and integer arrays containing board information
    with 0 noting an empty cavity '-' and 1 noting a cavity 'o'
    """
    with open(file) as f:
        boards = []
        cavities = []
        for line in f:
            board = []
            if len(line) == 2:
                boards.append(int(line[0])) #number of games (boards) to be played
            else:
                for char in line[0:12]:
                    board.append(0 if char == "-" else 1)

                boards.append(board)

    return boards

if __name__ == "__main__":
    main()