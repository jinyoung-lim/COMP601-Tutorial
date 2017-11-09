""" File: PebbleSolitaire.py
Author: JJ Lim
Date: Oct 2017 - Nov 2017

A class dedicated to solve "Pebble Solitaire" problem from Open Kattis (https://open.kattis.com/problems/pebblesolitaire).
"""

def main():
    boards = readPebbleFile("pebblesolitaire.in")
    for board in boards:
        print(dfsPebbles(board).count(1))


def dfsPebbles(board):
    '''Use depth-first search to move the cavities
    :param board: list of integers containing information about the pebble solitaire board. Empty pebbles are noted
     with 0, cavities are noted with 1.
    :return: a copy of the board after moving a cavity, return None if cannot move anymore
    '''
    boardCopy = board

    cavityInd = getCavityInds(board)

    while(cavityInd):
        currInd = cavityInd.pop()
        if (currInd < len(boardCopy)-3 and boardCopy[currInd + 1] == 1 and boardCopy[currInd + 2] == 0):
            moveRight(boardCopy, currInd)           # found the path to move right
            cavityInd = getCavityInds(boardCopy)    # update the cavityInd list

        if (currInd > 2 and boardCopy[currInd - 1] == 1 and boardCopy[currInd - 2] == 0):
            moveLeft(boardCopy, currInd)            # found the path to move right
            cavityInd = getCavityInds(boardCopy)    # update the cavityInd list

    return boardCopy


def getCavityInds(board):
    """ Get indexes of cavities in board list.
    :param board: list of integers containing information about the pebble solitaire board. Empty pebbles are noted
     with 0, cavities are noted with 1.
    :return: a list of integers containing indexes of cavities
    """
    cavityInd = []
    for i in range(0, len(board)):
        if board[i] == 1:
            cavityInd.append(i)
    return cavityInd


def moveLeft(board, cavityPos):
    """ Move a cavity left.
    :param board: list of integers containing information about the pebble solitaire board. Empty pebbles are noted
     with 0, cavities are noted with 1.
    :param cavityPos: index of the cavity to be moved left
    :return:
    """
    board[cavityPos] = 0
    board[cavityPos-1] = 0
    board[cavityPos-2] = 1


def moveRight(board, cavityPos):
    """ Move a cavity right.
    :param board: list of integers containing information about the pebble solitaire board. Empty pebbles are noted
     with 0, cavities are noted with 1.
    :param cavityPos: index of the cavity to be moved right
    :return:
    """
    board[cavityPos] = 0
    board[cavityPos+1] = 0
    board[cavityPos+2] = 1


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
        for line in f:
            board = []
            if len(line) != 2:  #actual boards, NOT number of games (boards) to be played
                for char in line[0:12]:
                    board.append(0 if char == "-" else 1)
                boards.append(board)

    return boards


if __name__ == "__main__":
    main()