""" File: KittenTree.py
Author: JJ Lim
Date: 9/27/2017 - 10/4/2017

A class dedicated to solve "Kitten on a Tree" problem from Open Kattis (https://open.kattis.com/problems/kitten).
"""
def main():
    branches = getBranches("test0.in")
    rescuePath = getRescuePath(branches)

    for step in rescuePath:
        print(step, end=" ")

def getBranches(inFile):
    """ Reads in the input file containing the tree information and returns the list containing roots (int) and their
    branches (int list)
    :param inFile: a file containing tree information with where the Kitten is and -1 denoting the end of file.
    :return: the list containing roots (int) and their branches (int list)
     a dictionary with keys as each branch's root and values as its children
    """

    with open(inFile) as f:
        branches = []
        for line in f:
            line = line.split()  # to deal with blank
            if line:  # lines (ie skip them)
                line = [int(i) for i in line]
                branches.append(line)
    return branches
    # Reading a file and converting str to int: https://stackoverflow.com/questions/12271503/python-read-numbers-from-text-file-and-put-into-list


def getRescuePath(branches):
    """ Finds the rescue path for the kitten on a tree.
    :param branches: a list containing roots (int) and their branches (int list)
    :return: a list of integers containing rescue path for the kitten
    """
    kit_loc = branches.pop(0)[0] # get the initial location of kitten
    branches.pop(len(branches)-1) # remove the last element, -1, which represents the end of the file


    rescuePath = []
    rescuePath.append(kit_loc)

    cleanBranches = [] # in even numbers, roots; in odd numbers branches
    for branch in branches:
        cleanBranches.append(branch[0])
        cleanBranches.append(branch[1:])

    grandRoot = getGrandRoot(cleanBranches)


    while (kit_loc != grandRoot):
        for branch in branches:
            if kit_loc in branch[1:]:
                kit_loc = branch[0]
                rescuePath.append(kit_loc)


    return rescuePath

def getGrandRoot(cleanBranches):
    """ Gets the Grand Root of the tree
    :param cleanBranches: a list that has roots as int type and their branches as int list type
    :return: the root of all roots and branches of the tree
    """
    for root in cleanBranches[::2]:
        for branches in cleanBranches[1::2]:
            if root in branches:
                break
        return root



if __name__ == "__main__":
    main()


