""" File: KittenTree.py
Author: JJ Lim
Date: 9/27/2017

A class dedicated to solve "Kitten on a Tree" problem from Open Kattis (https://open.kattis.com/problems/kitten).
"""
import re

def main():

    kitten_loc, treeDict = readTreeDict("test0.in")
    findPath(kitten_loc, treeDict)


def readTreeDict(inFile):
    """
    Reads in the input file containing the tree information.
    :param inFile: a file containing tree information with where the Kitten is and -1 denoting the end of file.
    :return: branch number of where the kitten is located, and
     a dictionary with keys as each branch's root and values as its children
    """
    lines = [line.rstrip('\n') for line in open(inFile)]
    kitten_loc = lines.pop(0)

    treeArray = [] #using dictionary does not seem to work...

    root_ind = 0

    for line in lines:

        if (line == "-1"):
            break
        else:
            branch = line.split(" ")
            treeArray[root_ind] = branch[0]
            # roots.append(branch[0])

    # print(treeDict)
    return kitten_loc, treeArray


def findPath(kitten_loc, treeDict):
    """Finds the rescue path for the kitten to get down from the tree to the ground.
    :param kitten_loc: branch number of where the kitten is located
    :param treeDict: a dictionary with keys as each branch's root and values as its children
    :return:
    """
    tree = treeDict

    roots = treeDict.keys()

    values = []
    for value in treeDict.values():
        while len(value) != 0:
            values.append(value.pop())

    GrandRoot = "-1"
    for root in roots:
        if root not in values:
            GrandRoot = root

    rescuePath = [kitten_loc]
    branch = kitten_loc

    while kitten_loc != GrandRoot:
        if branch in tree.values():
            rescuePath.append(tree.get(branch))
            print(tree.get(branch))
            kitten_loc = tree.get(branch)
        #
        # for branch in values:
        #     if branch == kitten_loc:
        #         rescuePath.append(tree.get(branch))
        #         kitten_loc = tree.get(branch)
    print(rescuePath)


if __name__ == "__main__":
    main()


