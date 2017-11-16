""" File: TreasureHunt.py
Author: JJ Lim
Date: Nov 2017

A class dedicated to solve "Treasure Hunt" problem from Open Kattis (https://open.kattis.com/problems/treasurehunt).
"""
import numpy as np

def main():
    """ If the player eventually reaches the treasure by following the directions, output a line containing an
    integer, the number of moves required to reach the treasure. If the directions cause the player to leave the playing
    area, output a line containing the word "Out". If the directions cause the player to stay in the playing area but
    never reach the treasure, output a line containing the word "Lost".
    :return:
    """
    print(treasureHunt("D.17.in"))
    print(treasureHunt("treasureHuntTest0.in"))
    print(treasureHunt("treasureHuntTest1.in"))
    print(treasureHunt("treasureHuntTest2.in"))


def treasureHunt(file):
    """ Reads the file using readFile(file) as a helper function and finds out if the player can reach the treasure, is
    lost, or out of the field. If the player eventually reaches the treasure by following the directions, output a line
    containing an integer, the number of moves required to reach the treasure. If the directions cause the player to
    leave the playing area, output a line containing the word "Out". If the directions cause the player to stay in the
    playing area but never reach the treasure, output a line containing the word "Lost"
    :param file: to be read with readFile(file) function
    :return: the number of moves if the treasure is found, "Lost" if not, "Out" if out of field
    """
    rowPos = 0
    colPos = 0

    matrix = readFile(file)

    countLeft = matrix.size
    while countLeft > 0:
        if rowPos >= matrix.shape[0] or colPos >= matrix.shape[1] or rowPos < 0 or colPos < 0:
            return "Out"

        if matrix.item((rowPos, colPos)) == 'N':
            rowPos -= 1
            countLeft -= 1
        elif matrix.item((rowPos, colPos)) == 'S':
            rowPos += 1
            countLeft -= 1
        elif matrix.item((rowPos, colPos)) == 'E':
            colPos += 1
            countLeft -= 1
        elif matrix.item((rowPos, colPos)) == 'W':
            colPos -= 1
            countLeft -= 1
        elif matrix.item((rowPos, colPos)) == 'T':
            return matrix.size - countLeft



    return "Lost"

def readFile(file):
    """ Reads in the file containing Treasure Hunt game information.

    :param file: containing the Treasure Hunt game information. The first line of input contains two integers R and C,
    each between 11 and 200200, inclusive. These integers define the number of rows and columns in the playing area,
    respectively. The next R lines of input describe the playing area. Each line contains exactly C letters, and each
    letter defines the action to take in each location in the playing area. There are five possible letters: N, S, W, E,
    and T.
    :return: a RXC multidimensional array in numpy.ndarray structure containing field information of the
    """
    with open(file) as f:
        r, c = [int(x) for x in next(f).split()]   # https://stackoverflow.com/questions/6583573/how-to-read-numbers-from-file-in-python
        if (r > 200 or c > 200 or r < 0 or c <0):
            # raise IndexError("Row and column value must be integers in range [1, 200]")
            exit("Row and column value must be integers in range [1, 200]")

        field = np.ndarray(shape=(r,c), dtype=np.object)

        i = 0
        for line in f:
            line = line.rstrip("\n")
            for char in line:
                field.flat[i] = char
                i += 1

    return field

if __name__ == "__main__":
    main()